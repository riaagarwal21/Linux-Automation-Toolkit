import os
import click
import zipfile
from datetime import datetime


def create_backup(source, dest):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.zip"
    backup_path = os.path.join(dest, backup_name)

    click.secho(f"\nCreating backup: {backup_path}", fg="blue")

    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=source)
                zipf.write(file_path, arcname)

    click.secho("Backup completed successfully!", fg="green")
    
    