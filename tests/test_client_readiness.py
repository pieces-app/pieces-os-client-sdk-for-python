from unittest.mock import Mock, patch

import pytest

from pieces_os_client.wrapper.client import PiecesClient


WEBSOCKET_URL_ATTRIBUTES = (
    "ASSETS_IDENTIFIERS_WS_URL",
    "AUTH_WS_URL",
    "ASK_STREAM_WS_URL",
    "CONVERSATION_WS_URL",
    "HEALTH_WS_URL",
    "ANCHORS_IDENTIFIERS_WS_URL",
    "LTM_VISION_WS_URL",
    "RANGES_IDENTIFIERS_WS_URL",
)


def make_client(port=""):
    client = PiecesClient.__new__(PiecesClient)
    client._port = port
    client._reconnect_on_host_change = False
    client._readiness_diagnostic = {
        "code": "PORT_UNSET",
        "message": "PiecesOS port is unset.",
    }
    return client


def assert_no_urls_created(client):
    assert not hasattr(client, "api_client")
    for attribute in WEBSOCKET_URL_ATTRIBUTES:
        assert not hasattr(client, attribute)


@pytest.mark.parametrize(
    ("raw_port", "expected_code"),
    [
        (None, "PORT_UNSET"),
        ("", "PORT_UNSET"),
        (" ", "PORT_UNSET"),
        ("null", "PORT_INVALID"),
        ("None", "PORT_INVALID"),
        ("abc", "PORT_INVALID"),
        ("39300/tcp", "PORT_INVALID"),
        ("0", "PORT_OUT_OF_RANGE"),
        ("65536", "PORT_OUT_OF_RANGE"),
    ],
)
def test_invalid_raw_ports_never_call_connect_apis(raw_port, expected_code):
    client = make_client()
    client.connect_apis = Mock()

    client.port = raw_port

    client.connect_apis.assert_not_called()
    assert client._readiness_diagnostic["code"] == expected_code


@pytest.mark.parametrize("raw_port", [None, "", " ", "null", "None"])
def test_invalid_raw_ports_never_create_rest_or_websocket_urls(raw_port):
    client = make_client(raw_port)

    with patch.object(client, "_port_scanning", return_value=raw_port):
        with pytest.raises(ValueError):
            _ = client.host

    assert_no_urls_created(client)


@pytest.mark.parametrize(
    "host",
    [
        "http://127.0.0.1:",
        "http://127.0.0.1:null",
        "http://127.0.0.1:None",
        "http://127.0.0.1:0",
    ],
)
def test_malformed_hosts_never_create_rest_or_websocket_urls(host):
    client = make_client()

    with pytest.raises(TypeError):
        client.connect_apis(host)

    assert client._readiness_diagnostic["code"] == "PORT_INVALID"
    assert_no_urls_created(client)


def test_scan_failure_stores_port_scan_failed():
    client = make_client()

    with patch.object(PiecesClient, "_probe_pieces_os_port", return_value=(None, None, None)):
        with pytest.raises(ValueError, match="PORT_SCAN_FAILED"):
            client._port_scanning()

    assert client._readiness_diagnostic["code"] == "PORT_SCAN_FAILED"


def test_scan_health_probe_failure_stores_port_health_probe_failed():
    client = make_client()

    with patch.object(
        PiecesClient,
        "_probe_pieces_os_port",
        return_value=("PORT_HEALTH_PROBE_FAILED", None, "probe failed"),
    ):
        with pytest.raises(ValueError, match="PORT_HEALTH_PROBE_FAILED"):
            client._port_scanning()

    assert client._readiness_diagnostic["code"] == "PORT_HEALTH_PROBE_FAILED"


def test_ready_probe_stores_port_ready_and_valid_host():
    client = make_client()

    with patch.object(
        PiecesClient,
        "_probe_pieces_os_port",
        return_value=("PORT_READY", "39300", None),
    ):
        assert client._port_scanning() == "39300"

    assert client._readiness_diagnostic["code"] == "PORT_READY"
    assert client._readiness_diagnostic["host"] == "http://127.0.0.1:39300"


def test_is_pieces_running_health_probe_failure_stores_diagnostic():
    client = make_client("39300")

    with patch(
        "pieces_os_client.wrapper.client.urllib.request.urlopen",
        side_effect=OSError("connection refused"),
    ):
        assert client.is_pieces_running() is False

    assert client._readiness_diagnostic["code"] == "PORT_HEALTH_PROBE_FAILED"


def test_is_pieces_running_ready_probe_stores_port_ready_and_valid_host():
    class HealthyResponse:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, traceback):
            return False

    client = make_client("39300")

    with patch(
        "pieces_os_client.wrapper.client.urllib.request.urlopen",
        return_value=HealthyResponse(),
    ):
        assert client.is_pieces_running() is True

    assert client._readiness_diagnostic["code"] == "PORT_READY"
    assert client._readiness_diagnostic["host"] == "http://127.0.0.1:39300"


def test_port_none_reset_behavior_remains_safe():
    client = make_client("39300")
    client.connect_apis = Mock()

    client.port = None

    client.connect_apis.assert_not_called()
    assert client._port is None
    assert client._readiness_diagnostic["code"] == "PORT_UNSET"
    assert_no_urls_created(client)
