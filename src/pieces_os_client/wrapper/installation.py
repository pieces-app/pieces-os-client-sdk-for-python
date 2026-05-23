import sys
import subprocess
import platform
from enum import Enum
from tempfile import gettempdir
import re
import threading
import time
from typing import List, Optional, Tuple, Callable

import urllib.request

class PlatformEnum(Enum):
    Windows = 'Windows'
    Linux = 'Linux'
    Macos = 'Macos'

class DownloadState(Enum):
    IDLE = 'IDLE'
    DOWNLOADING = 'DOWNLOADING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'

class TerminalEventType(Enum):
    PROMPT = 'PROMPT'
    OUTPUT = 'OUTPUT'
    ERROR = 'ERROR'

class DownloadModel:
    def __init__(
        self,
        state: DownloadState,
        terminal_event: TerminalEventType,
        bytes_received: int = 0,
        total_bytes: int = 0,
        percent: float = 0,
        message: Optional[str] = None,
        error: Optional[str] = None,
        error_code: Optional[str] = None,
        command: Optional[List[str]] = None,
        return_code: Optional[int] = None,
        url: Optional[str] = None,
    ):
        self.bytes_received = bytes_received
        self.total_bytes = total_bytes
        self.percent = percent
        self.state = state
        self.terminal_event = terminal_event
        self.message = message
        self.error = error
        self.error_code = error_code
        self.command = command
        self.return_code = return_code
        self.url = url

class PosInstaller:
    MACOS_INTEL_PACKAGE_SLUG = 'pkg-pos-launch-only'
    MACOS_ARM_PACKAGE_SLUG = 'pkg-pos-launch-only-arm64'

    def __init__(self, callback: Optional[Callable[[DownloadModel], None]], product: str):
        self.platform = self.detect_platform()
        self.download_process = None
        self.progress_update_callback = callback
        self.state = DownloadState.IDLE
        self.terminal_event = TerminalEventType.PROMPT
        self.stop = False
        self.thread = None
        self.product = product


    def update_progress(
        self,
        bytes_received: int = 0,
        total_bytes: int = 0,
        message: Optional[str] = None,
        error: Optional[str] = None,
        error_code: Optional[str] = None,
        command: Optional[List[str]] = None,
        return_code: Optional[int] = None,
        url: Optional[str] = None,
    ):
        if self.progress_update_callback:
            if total_bytes == 0:
                percent = 0
            else:
                percent = (bytes_received/total_bytes)*100
            progress = DownloadModel(
                self.state,
                self.terminal_event,
                bytes_received,
                total_bytes,
                percent,
                message=message,
                error=error,
                error_code=error_code,
                command=command,
                return_code=return_code,
                url=url,
            )
            self.progress_update_callback(progress)

    def _emit_failure(
        self,
        error_code: str,
        message: str,
        error: Optional[str] = None,
        command: Optional[List[str]] = None,
        return_code: Optional[int] = None,
        url: Optional[str] = None,
    ) -> None:
        self.state = DownloadState.FAILED
        self.terminal_event = TerminalEventType.ERROR
        self.update_progress(
            message=message,
            error=error or message,
            error_code=error_code,
            command=command,
            return_code=return_code,
            url=url,
        )

    @staticmethod
    def detect_platform() -> PlatformEnum:
        if sys.platform == 'win32':
            return PlatformEnum.Windows
        elif sys.platform == 'linux':
            return PlatformEnum.Linux
        else:
            return PlatformEnum.Macos

    def start_download(self) -> bool:
        if self.state == DownloadState.DOWNLOADING:
            return False

        self.state = DownloadState.DOWNLOADING
        self.update_progress()
        self.thread = threading.Thread(target=self._start_download, daemon=True)
        self.thread.start()
        return True

    def _start_download(self):
        try:
            if self.platform == PlatformEnum.Windows:
                self.download_windows()
            elif self.platform == PlatformEnum.Linux:
                self.download_linux()
            elif self.platform == PlatformEnum.Macos:
                self.download_macos()
        except Exception as e:
            self._emit_failure(
                'INSTALLER_UNHANDLED_ERROR',
                f'Unexpected installer error: {e}',
                error=str(e),
            )

    def download_linux(self):
        self.print('Starting POS download for Linux.')
        command = '''
            if command -v pkexec >/dev/null 2>&1; then
              pkexec snap install pieces-os && \
              pkexec snap connect pieces-os:process-control :process-control && \
              pieces-os
            else
              echo "Error: pkexec is not available. Exiting." >&2
              exit 1
            fi
        '''
        return self.execute_command('bash', '-c', [command], self.extract_linux_regex)

    def download_macos(self):
        self.print('Starting POS download for Macos.')

        try:
            package_slug = self._resolve_macos_package_slug()
        except ValueError as e:
            self._emit_failure(
                'MACOS_UNSUPPORTED_ARCHITECTURE',
                str(e),
                error=str(e),
            )
            return False

        pkg_url = f'https://builds.pieces.app/stages/production/macos_packaging/{package_slug}/download?product={self.product}&download=true'
        tmp_pkg_path = "/tmp/Pieces-OS-Launch.pkg"
        return self.install_using_web(pkg_url, tmp_pkg_path)

    def download_windows(self):
        self.print('Starting POS download for Windows.')
        pkg_url = f'https://builds.pieces.app/stages/production/os_server/windows-exe/download?download=true&product={self.product}'
        tmp_pkg_path = f"{gettempdir()}\\Pieces-OS.exe"
        return self.install_using_web(pkg_url, tmp_pkg_path)

    @staticmethod
    def _detect_macos_cpu_architecture() -> str:
        return platform.machine().lower()

    @staticmethod
    def _is_apple_silicon_hardware() -> bool:
        if sys.platform != 'darwin':
            return False

        try:
            output = subprocess.check_output(
                ['/usr/sbin/sysctl', '-n', 'hw.optional.arm64'],
                stderr=subprocess.DEVNULL,
                timeout=2,
            )
            return output.decode('utf-8').strip() == '1'
        except (subprocess.SubprocessError, OSError, UnicodeDecodeError):
            return False

    @classmethod
    def _resolve_macos_package_slug(cls, machine: Optional[str] = None) -> str:
        architecture = (machine or cls._detect_macos_cpu_architecture()).lower().replace('-', '_')

        if architecture in ('arm64', 'aarch64'):
            return cls.MACOS_ARM_PACKAGE_SLUG

        if architecture in ('x86_64', 'amd64', 'i386', 'i686'):
            if architecture in ('x86_64', 'amd64') and cls._is_apple_silicon_hardware():
                return cls.MACOS_ARM_PACKAGE_SLUG
            return cls.MACOS_INTEL_PACKAGE_SLUG

        raise ValueError(f'Unsupported macOS CPU architecture: {architecture or "unknown"}')

    def install_using_web(self, pkg_url: str, tmp_pkg_path: str) -> bool:
        BUFFER_SIZE = 65536
        STALL_TIMEOUT = 5

        try:
            self.state = DownloadState.DOWNLOADING
            request = urllib.request.Request(pkg_url, headers={'Accept': '*/*'})
            response = urllib.request.urlopen(request)
            file_size = int(response.info().get('Content-Length', 0))
            downloaded_size = 0

            with open(tmp_pkg_path, 'wb') as out_file:
                last_data_time = time.time()
                while True:
                    data = response.read(BUFFER_SIZE)
                    if not data:
                        break
                    if self.stop:
                        self.print("Download stopped by user.")
                        self.update_progress_stop()
                        return False

                    out_file.write(data)
                    downloaded_size += len(data)
                    last_data_time = time.time()

                    if downloaded_size % (512 * 1024) == 0 or downloaded_size == file_size:
                        self.update_progress(downloaded_size, file_size)
                        self.print(f'Downloaded {downloaded_size} of {file_size}')
                    if time.time() - last_data_time > STALL_TIMEOUT:
                        raise TimeoutError("Download stalled (no data received).")

                    self.update_progress(downloaded_size, file_size)
                    self.print(f'Downloaded {downloaded_size} of {file_size}')

            self.print(f'Download completed. Opening {tmp_pkg_path}.')
            if sys.platform == 'win32':
                command = ['start', tmp_pkg_path]
                result = subprocess.run(command, shell=True)
            else:
                command = ['open', tmp_pkg_path]
                result = subprocess.run(command)

            return_code = getattr(result, 'returncode', 0)
            if return_code != 0:
                self._emit_failure(
                    'INSTALLER_LAUNCH_FAILED',
                    f'Installer launch command failed with exit code {return_code}.',
                    command=command,
                    return_code=return_code,
                    url=pkg_url,
                )
                return False

            self.state = DownloadState.COMPLETED
            self.update_progress(url=pkg_url, message=f'Download completed. Opened {tmp_pkg_path}.')
            return True
        except Exception as e:
            self._emit_failure(
                'DOWNLOAD_FAILED',
                f'Error downloading POS: {e}',
                error=str(e),
                url=pkg_url,
            )
            self.print(f'Error downloading POS: {e}')
            return False


    def extract_linux_regex(self, line) -> Optional[Tuple[int, int]]:
        pattern = r"(\d+)%\s+([\d.]+)MB/s\s+([\dms.]+)"

        match = re.search(pattern, line)

        if match:
            percentage = match.group(1)
            download_speed = match.group(2)
            time_remaining = match.group(3)
            total_bytes = int(download_speed) * int(time_remaining)
            bytes_downloaded = (int(percentage) / 100) * total_bytes

            return bytes_downloaded, total_bytes

    def execute_command(self, shell: str, command: str, args: List[str], callback: Optional[Callable[[str], Tuple[int, int]]]) -> bool:
        command_parts = [shell, command] + args
        stderr_lines = []
        try:
            self.print(f'Spawning process: {shell} {command} {args}')
            self.download_process = subprocess.Popen(
                command_parts,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            def decode_line(raw_line) -> str:
                if isinstance(raw_line, bytes):
                    return raw_line.decode('utf-8', errors='replace').strip()
                return str(raw_line).strip()

            def read_stdout() -> None:
                while True:
                    raw_line = self.download_process.stdout.readline()
                    if not raw_line:
                        break
                    line = decode_line(raw_line)
                    if not line:
                        continue
                    self.state = DownloadState.DOWNLOADING
                    self.terminal_event = TerminalEventType.OUTPUT
                    try:
                        bytes_received, total_bytes = callback(line) if callback else (0, 0)
                        self.print(f'Downloaded {bytes_received} of {total_bytes}')
                        self.update_progress(bytes_received, total_bytes)
                    except Exception as e:
                        self.print(f"Could not match pattern: {e}", file=sys.stderr)

            def read_stderr() -> None:
                while True:
                    raw_line = self.download_process.stderr.readline()
                    if not raw_line:
                        break
                    line = decode_line(raw_line)
                    if not line:
                        continue
                    stderr_lines.append(line)

            stdout_thread = threading.Thread(target=read_stdout, daemon=True)
            stderr_thread = threading.Thread(target=read_stderr, daemon=True)
            stdout_thread.start()
            stderr_thread.start()

            return_code = self.download_process.wait()
            stdout_thread.join()
            stderr_thread.join()
            if return_code != 0:
                stderr_text = "\n".join(stderr_lines)
                message = f'Command failed with exit code {return_code}.'
                if stderr_text:
                    message = f'{message} stderr: {stderr_text}'
                self._emit_failure(
                    'COMMAND_FAILED',
                    message,
                    error=message,
                    command=command_parts,
                    return_code=return_code,
                )
                return False

            self.print('Process completed.')
            return True
        except Exception as e:
            self.print(f'Error executing command: {e}')
            self._emit_failure(
                'COMMAND_EXECUTION_FAILED',
                f'Error executing command: {e}',
                error=str(e),
                command=command_parts,
            )
            return False


    def cancel_download(self) -> None:
        if self.state == DownloadState.DOWNLOADING:
            if self.download_process:
                self.download_process.kill()
                self.update_progress_stop()
            else:
                self.stop = True

    def update_progress_stop(self) -> None:
        self.state = DownloadState.IDLE
        self.terminal_event = TerminalEventType.OUTPUT
        self.update_progress()
        self.print('Download canceled.')

    def print(self, message, file=sys.stdout): # for debugging
        return
        # print(message, file=file)