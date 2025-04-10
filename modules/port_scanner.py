import click
import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((target, port))
            return port, True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return port, False


def scan_ports(target, ports="1-1024"):
    start_port, end_port = map(int, ports.split("-"))
    open_ports = []

    click.secho(f"\nScanning {target} (Ports: {start_port}-{end_port})...", fg="yellow")

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            try:
                port, is_open = future.result()
                if is_open:
                    open_ports.append(port)
                    click.secho(f"  Port {port}: OPEN", fg="green")
            except Exception as e:
                click.secho(f"  [!] Error scanning port: {e}", fg="red")

    click.secho(f"\nFound {len(open_ports)} open ports.", fg="cyan")


# Export for testing
__all__ = ["scan_ports", "scan_port"]
