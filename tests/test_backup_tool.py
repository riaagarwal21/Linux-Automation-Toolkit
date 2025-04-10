import os
from modules import backup_tool


def test_create_backup_creates_file(tmp_path):
    test_dir = tmp_path / "data"
    test_dir.mkdir()
    test_file = test_dir / "file.txt"
    test_file.write_text("hello")

    backup_tool.create_backup(str(test_dir), str(tmp_path))

    zip_files = list(tmp_path.glob("*.zip"))
    assert len(zip_files) == 1

