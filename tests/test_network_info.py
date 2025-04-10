from modules import network_info


def test_display_network_info_runs_without_ping():
    network_info.display_network_info(ping_check=False)


def test_network_ping_fails(monkeypatch):
    from modules import network_info
    import subprocess

    def mock_run(*args, **kwargs):
        raise subprocess.CalledProcessError(1, cmd=args[0])
    
    monkeypatch.setattr("subprocess.run", mock_run)
    network_info.display_network_info(ping_check=True)

