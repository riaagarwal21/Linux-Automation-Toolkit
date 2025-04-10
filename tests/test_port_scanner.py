import socket
import pytest
from modules import port_scanner


def test_scan_specific_open_port(monkeypatch):
    def mock_scan_port(target, port):
        return port, True

    monkeypatch.setattr("modules.port_scanner.scan_port", mock_scan_port)
    port_scanner.scan_ports("127.0.0.1", "80-80")


def test_scan_specific_closed_port(monkeypatch):
    def mock_scan_port(target, port):
        return port, False

    monkeypatch.setattr("modules.port_scanner.scan_port", mock_scan_port)
    port_scanner.scan_ports("127.0.0.1", "81-81")


def test_scan_port_raises(monkeypatch):
    def mock_scan_port(target, port):
        raise socket.timeout("Timeout")

    monkeypatch.setattr("modules.port_scanner.scan_port", mock_scan_port)
    port_scanner.scan_ports("127.0.0.1", "9999-9999")

