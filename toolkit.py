import click
from config import settings
from modules import network_info, system_monitor, port_scanner, backup_tool

@click.group()
def cli():
    """Linux System Automation Toolkit."""
    pass

@cli.command()
@click.option("--ping", is_flag=True, help="Check network connectivity via ping")
def network(ping):
    """Display IP, MAC, gateway, and DNS info."""
    network_info.display_network_info(ping)

@cli.command()
def monitor():
    """Monitor CPU, RAM, and disk usage."""
    system_monitor.display_system_stats()

@cli.command()
@click.argument("target")
@click.option("-p", "--ports", default=settings.DEFAULT_PORT_RANGE, help="Port range (e.g., 1-1000)")
def scan(target, ports):
    """Scan for open TCP ports on a target."""
    port_scanner.scan_ports(target, ports)

@cli.command()
@click.argument("source")
@click.option("-d", "--dest", default=settings.DEFAULT_BACKUP_DEST, help="Backup destination path")
def backup(source, dest):
    """Backup a directory to a ZIP file."""
    backup_tool.create_backup(source, dest)

if __name__ == "__main__":
    cli()
