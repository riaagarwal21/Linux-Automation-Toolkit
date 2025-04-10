import click
import psutil
import socket
import subprocess
from config import settings


def display_network_info(ping_check=False):
    click.secho("\n=== Network Information ===", fg="blue", bold=True)
    
    for name, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                click.echo(f"Interface: {click.style(name, fg='yellow')}")
                click.echo(f"  IP: {addr.address}")
                click.echo(f"  MAC: {addrs[0].address if addrs else 'N/A'}")

    gateways = psutil.net_if_stats()
    default_gateway = next((name for name, stats in gateways.items() if stats.isup), None)
    click.echo(f"\nDefault Gateway: {click.style(default_gateway, fg='cyan')}")

    if ping_check:
        try:
            subprocess.run(["ping", "-c", "4", settings.DEFAULT_PING_ADDRESS], check=True, stdout=subprocess.PIPE)
            click.secho("Ping Check: Success", fg="green")
        except subprocess.CalledProcessError:
            click.secho("Ping Check: Failed", fg="red")
            
            