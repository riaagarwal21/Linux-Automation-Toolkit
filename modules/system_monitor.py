import psutil
import click


def display_system_stats():
    click.secho("\n=== System Monitor ===", fg="blue", bold=True)

    cpu = psutil.cpu_percent(interval=1)
    click.echo(f"CPU Usage: {click.style(f'{cpu}%', fg='red' if cpu > 80 else 'green')}")

    mem = psutil.virtual_memory()
    click.echo(f"RAM Usage: {click.style(f'{mem.percent}%', fg='red' if mem.percent > 80 else 'green')}")

    disk = psutil.disk_usage('/')
    click.echo(f"Disk Usage: {click.style(f'{disk.percent}%', fg='red' if disk.percent > 90 else 'green')}")

