import re
import subprocess
import sys

from typer.testing import CliRunner

from examples.cli import app

runner = CliRunner()


def test_cli_main_default():
    """Test the CLI main command with default options."""
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Hello World!" in result.stdout
    assert (
        "Core library says: Hello, World! This greeting comes from 'your_core_library'."
        in result.stdout
    )
    assert "Printed the greeting 1 time(s) for World." in result.stdout


def test_cli_main_custom_name():
    """Test the CLI main command with a custom name."""
    result = runner.invoke(app, ["--name", "Cascade"])
    assert result.exit_code == 0
    assert "Hello Cascade!" in result.stdout
    assert (
        "Core library says: Hello, Cascade! This greeting comes from 'your_core_library'."
        in result.stdout
    )
    assert "Printed the greeting 1 time(s) for Cascade." in result.stdout


def test_cli_main_custom_count():
    """Test the CLI main command with a custom count."""
    result = runner.invoke(app, ["--count", "2"])
    assert result.exit_code == 0
    assert "Hello World!" in result.stdout
    core_message = (
        "Core library says: Hello, World! This greeting comes from 'your_core_library'."
    )
    # Check if the core message appears twice
    assert result.stdout.count(core_message) == 2
    assert "Printed the greeting 2 time(s) for World." in result.stdout


def test_cli_main_custom_name_and_count():
    """Test the CLI main command with custom name and count."""
    result = runner.invoke(app, ["--name", "Tester", "--count", "3"])
    assert result.exit_code == 0
    assert "Hello Tester!" in result.stdout
    core_message = "Core library says: Hello, Tester! This greeting comes from 'your_core_library'."
    assert result.stdout.count(core_message) == 3
    assert "Printed the greeting 3 time(s) for Tester." in result.stdout


# It's good practice to also test the --help option
def test_cli_help():
    """Test the CLI --help option using subprocess."""
    # MODIFIED: Use subprocess.run to invoke the script
    script_path = "examples/cli.py"  # Path to the CLI script
    python_executable = sys.executable  # Path to current python interpreter

    result = subprocess.run(
        [python_executable, script_path, "--help"],
        capture_output=True,
        text=True,
        check=False,  # Don't raise exception on non-zero exit, we'll assert it
    )

    # Strip ANSI escape codes from stdout for more robust assertions
    # Pattern for ANSI escape codes
    ansi_escape_pattern = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-9:;<=>?]*[ -/]*[@-~])")
    cleaned_stdout = ansi_escape_pattern.sub("", result.stdout)

    assert result.returncode == 0
    assert "Usage:" in cleaned_stdout
    assert (
        "Say hello and demonstrate core library functionality." in cleaned_stdout
    )  # MODIFIED: Check for command description
    # Add more assertions as needed, e.g., checking for specific options
    assert "--name" in cleaned_stdout
    assert "--count" in cleaned_stdout
