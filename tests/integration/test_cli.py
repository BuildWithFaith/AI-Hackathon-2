import subprocess


def run_cli(*args):
    # Using python -m src.cli.main
    cmd = ["python3", "-m", "src.cli.main"] + list(args)
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result


def test_cli_create_task():
    result = run_cli("create", "Buy milk", "--notes", "2 percent")
    assert result.returncode == 0
    assert "Task created" in result.stdout
    assert "Buy milk" in result.stdout


def test_cli_list_tasks():
    # Since CLI is stateless unless interactive, test empty state
    result = run_cli("list")
    assert result.returncode == 0
    assert "No tasks found" in result.stdout


def test_cli_get_not_found():
    result = run_cli("get", "invalid-id")
    assert "Error: Task with id invalid-id not found" in result.stdout


def test_cli_complete_not_found():
    result = run_cli("complete", "invalid-id")
    assert "Error: Task with id invalid-id not found" in result.stdout


def test_cli_delete_not_found():
    result = run_cli("delete", "invalid-id")
    assert "Error: Task with id invalid-id not found" in result.stdout
