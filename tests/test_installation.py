import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import MagicMock, mock_open, patch

INSTALLATION_PATH = (
    Path(__file__).resolve().parents[1]
    / "src"
    / "pieces_os_client"
    / "wrapper"
    / "installation.py"
)

spec = importlib.util.spec_from_file_location("installation_under_test", INSTALLATION_PATH)
installation = importlib.util.module_from_spec(spec)
sys.modules["installation_under_test"] = installation
spec.loader.exec_module(installation)

DownloadModel = installation.DownloadModel
DownloadState = installation.DownloadState
PosInstaller = installation.PosInstaller
TerminalEventType = installation.TerminalEventType


class TestPosInstallerMacosArchitecture(unittest.TestCase):
    def test_arm_cpu_uses_arm_launch_only_slug(self):
        self.assertEqual(
            PosInstaller._resolve_macos_package_slug("arm64"),
            PosInstaller.MACOS_ARM_PACKAGE_SLUG,
        )
        self.assertEqual(
            PosInstaller._resolve_macos_package_slug("aarch64"),
            PosInstaller.MACOS_ARM_PACKAGE_SLUG,
        )

    def test_intel_cpu_uses_intel_launch_only_slug(self):
        with patch.object(PosInstaller, "_is_apple_silicon_hardware", return_value=False):
            self.assertEqual(
                PosInstaller._resolve_macos_package_slug("x86_64"),
                PosInstaller.MACOS_INTEL_PACKAGE_SLUG,
            )
            self.assertEqual(
                PosInstaller._resolve_macos_package_slug("amd64"),
                PosInstaller.MACOS_INTEL_PACKAGE_SLUG,
            )

    def test_rosetta_intel_python_on_apple_silicon_uses_arm_slug(self):
        with patch.object(installation.sys, "platform", "darwin"):
            with patch.object(installation.subprocess, "check_output", return_value=b"1\n"):
                self.assertEqual(
                    PosInstaller._resolve_macos_package_slug("x86_64"),
                    PosInstaller.MACOS_ARM_PACKAGE_SLUG,
                )

    def test_unknown_macos_architecture_fails_before_download(self):
        events = []
        installer = PosInstaller(events.append, "TEST_PRODUCT")

        with patch.object(PosInstaller, "_detect_macos_cpu_architecture", return_value="sparc"):
            with patch.object(installer, "install_using_web") as install_using_web:
                result = installer.download_macos()

        self.assertFalse(result)
        install_using_web.assert_not_called()
        self.assertEqual(events[-1].state, DownloadState.FAILED)
        self.assertEqual(events[-1].terminal_event, TerminalEventType.ERROR)
        self.assertEqual(events[-1].error_code, "MACOS_UNSUPPORTED_ARCHITECTURE")
        self.assertIn("sparc", events[-1].error)

    def test_download_macos_uses_resolved_package_slug_and_tmp_path(self):
        installer = PosInstaller(None, "TEST_PRODUCT")

        with patch.object(
            PosInstaller,
            "_resolve_macos_package_slug",
            return_value=PosInstaller.MACOS_ARM_PACKAGE_SLUG,
        ):
            with patch.object(installer, "install_using_web", return_value=True) as install_using_web:
                result = installer.download_macos()

        self.assertTrue(result)
        pkg_url, tmp_pkg_path = install_using_web.call_args.args
        self.assertIn("macos_packaging/pkg-pos-launch-only-arm64/download", pkg_url)
        self.assertIn("product=TEST_PRODUCT", pkg_url)
        self.assertEqual(tmp_pkg_path, "/tmp/Pieces-OS-Launch.pkg")


class TestInstallerDiagnostics(unittest.TestCase):
    def test_download_model_keeps_existing_fields_and_adds_optional_diagnostics(self):
        model = DownloadModel(
            DownloadState.DOWNLOADING,
            TerminalEventType.PROMPT,
            5,
            10,
            50,
        )

        self.assertEqual(model.bytes_received, 5)
        self.assertEqual(model.total_bytes, 10)
        self.assertEqual(model.percent, 50)
        self.assertEqual(model.state, DownloadState.DOWNLOADING)
        self.assertEqual(model.terminal_event, TerminalEventType.PROMPT)
        self.assertIsNone(model.message)
        self.assertIsNone(model.error)
        self.assertIsNone(model.error_code)
        self.assertIsNone(model.command)
        self.assertIsNone(model.return_code)
        self.assertIsNone(model.url)

        diagnostic = DownloadModel(
            DownloadState.FAILED,
            TerminalEventType.ERROR,
            message="failed",
            error="boom",
            error_code="DOWNLOAD_FAILED",
            command=["open", "/tmp/Pieces-OS-Launch.pkg"],
            return_code=1,
            url="https://example.invalid/package",
        )

        self.assertEqual(diagnostic.message, "failed")
        self.assertEqual(diagnostic.error, "boom")
        self.assertEqual(diagnostic.error_code, "DOWNLOAD_FAILED")
        self.assertEqual(diagnostic.command, ["open", "/tmp/Pieces-OS-Launch.pkg"])
        self.assertEqual(diagnostic.return_code, 1)
        self.assertEqual(diagnostic.url, "https://example.invalid/package")

    def test_urlopen_exception_surfaces_failed_callback_diagnostics(self):
        events = []
        installer = PosInstaller(events.append, "TEST_PRODUCT")

        with patch.object(installation.urllib.request, "urlopen", side_effect=RuntimeError("network down")):
            result = installer.install_using_web("https://example.invalid/package", "/tmp/package.pkg")

        self.assertFalse(result)
        self.assertEqual(events[-1].state, DownloadState.FAILED)
        self.assertEqual(events[-1].terminal_event, TerminalEventType.ERROR)
        self.assertEqual(events[-1].error_code, "DOWNLOAD_FAILED")
        self.assertEqual(events[-1].error, "network down")
        self.assertEqual(events[-1].url, "https://example.invalid/package")

    def test_launcher_failure_surfaces_command_return_code_and_url(self):
        events = []
        installer = PosInstaller(events.append, "TEST_PRODUCT")
        response = MagicMock()
        response.info.return_value.get.return_value = "3"
        response.read.side_effect = [b"abc", b""]

        with patch.object(installation.urllib.request, "urlopen", return_value=response):
            with patch("builtins.open", mock_open()):
                with patch.object(installation.sys, "platform", "darwin"):
                    with patch.object(
                        installation.subprocess,
                        "run",
                        return_value=subprocess.CompletedProcess(["open", "/tmp/package.pkg"], 1),
                    ):
                        result = installer.install_using_web(
                            "https://example.invalid/package",
                            "/tmp/package.pkg",
                        )

        self.assertFalse(result)
        self.assertEqual(events[-1].state, DownloadState.FAILED)
        self.assertEqual(events[-1].error_code, "INSTALLER_LAUNCH_FAILED")
        self.assertEqual(events[-1].command, ["open", "/tmp/package.pkg"])
        self.assertEqual(events[-1].return_code, 1)
        self.assertEqual(events[-1].url, "https://example.invalid/package")

    def test_linux_stderr_and_nonzero_exit_are_callback_diagnostics(self):
        events = []
        call_order = []
        installer = PosInstaller(events.append, "TEST_PRODUCT")
        process = MagicMock()
        process.stdout = io.BytesIO(b"")
        process.stderr = io.BytesIO(b"pkexec is not available\n")
        process.wait.side_effect = lambda: call_order.append("wait") or 1
        installer.progress_update_callback = lambda event: (
            call_order.append("callback"),
            events.append(event),
        )

        with patch.object(installation.subprocess, "Popen", return_value=process):
            result = installer.execute_command(
                "bash",
                "-c",
                ["echo error >&2; exit 1"],
                lambda line: (0, 0),
            )

        self.assertFalse(result)
        self.assertEqual(call_order, ["wait", "callback"])
        self.assertEqual(len(events), 1)
        self.assertEqual(events[-1].state, DownloadState.FAILED)
        self.assertEqual(events[-1].terminal_event, TerminalEventType.ERROR)
        self.assertEqual(events[-1].error_code, "COMMAND_FAILED")
        self.assertEqual(events[-1].return_code, 1)
        self.assertIn("pkexec is not available", events[-1].message)
        self.assertIn("pkexec is not available", events[-1].error)
        self.assertEqual(events[-1].command, ["bash", "-c", "echo error >&2; exit 1"])

    def test_execute_command_preserves_stdout_progress_callbacks(self):
        events = []
        installer = PosInstaller(events.append, "TEST_PRODUCT")
        process = MagicMock()
        process.stdout = io.BytesIO(b"download progress\n")
        process.stderr = io.BytesIO(b"")
        process.wait.return_value = 0

        with patch.object(installation.subprocess, "Popen", return_value=process):
            result = installer.execute_command(
                "bash",
                "-c",
                ["echo download progress"],
                lambda line: (25, 100),
            )

        self.assertTrue(result)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].state, DownloadState.DOWNLOADING)
        self.assertEqual(events[0].terminal_event, TerminalEventType.OUTPUT)
        self.assertEqual(events[0].bytes_received, 25)
        self.assertEqual(events[0].total_bytes, 100)

    def test_execute_command_stderr_only_zero_exit_does_not_emit_error_callback(self):
        events = []
        installer = PosInstaller(events.append, "TEST_PRODUCT")
        process = MagicMock()
        process.stdout = io.BytesIO(b"")
        process.stderr = io.BytesIO(b"benign warning\n")
        process.wait.return_value = 0

        with patch.object(installation.subprocess, "Popen", return_value=process):
            result = installer.execute_command(
                "bash",
                "-c",
                ["echo warning >&2"],
                lambda line: (0, 0),
            )

        self.assertTrue(result)
        self.assertFalse(
            any(event.terminal_event == TerminalEventType.ERROR for event in events)
        )


if __name__ == "__main__":
    unittest.main()
