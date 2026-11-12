import subprocess
import sys

import pytest


def run_cli(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "calculator", *arguments],
        capture_output=True,
        text=True,
        check=False,
    )


@pytest.mark.parametrize(
    ("operation", "first", "second", "expected"),
    [
        ("add", "2", "3", "5\n"),
        ("subtract", "8", "3", "5\n"),
        ("multiply", "4", "3", "12\n"),
        ("divide", "12", "3", "4.0\n"),
        ("power", "2", "3", "8\n"),
    ],
)
def test_cli_operations_succeed(operation, first, second, expected):
    result = run_cli(operation, first, second)

    assert result.returncode == 0
    assert result.stdout == expected
    assert result.stderr == ""


def test_cli_supports_decimal_and_negative_values():
    result = run_cli("multiply", "-2.5", "4")

    assert result.returncode == 0
    assert float(result.stdout) == pytest.approx(-10)
    assert result.stderr == ""


def test_cli_preserves_large_integer_precision():
    result = run_cli("add", "9007199254740992", "1")

    assert result.returncode == 0
    assert result.stdout == "9007199254740993\n"
    assert result.stderr == ""


def test_cli_preserves_negative_integer_operands():
    result = run_cli("add", "-9007199254740992", "-1")

    assert result.returncode == 0
    assert result.stdout == "-9007199254740993\n"
    assert result.stderr == ""


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        ("0.1", "0.2", 0.3),
        ("1e3", "2.5e-1", 1000.25),
    ],
)
def test_cli_parses_decimal_and_scientific_notation_as_float(
    first, second, expected
):
    result = run_cli("add", first, second)

    assert result.returncode == 0
    assert float(result.stdout) == pytest.approx(expected)
    assert result.stderr == ""


def test_cli_preserves_large_integer_exponentiation():
    result = run_cli("power", "9007199254740992", "2")

    assert result.returncode == 0
    assert result.stdout == "81129638414606681695789005144064\n"
    assert result.stderr == ""


@pytest.mark.parametrize(
    ("operation", "first", "second", "expected"),
    [
        ("add", "-2", "-3", -5),
        ("subtract", "-2", "3", -5),
        ("divide", "-12", "3", -4),
        ("power", "-2", "3", -8),
        ("add", "0.1", "0.2", 0.3),
        ("subtract", "0.3", "0.1", 0.2),
        ("divide", "1.5", "0.5", 3),
        ("power", "2.5", "2", 6.25),
        ("power", "2", "-3", 0.125),
        ("add", "0", "7", 7),
        ("subtract", "0", "4", -4),
        ("multiply", "9", "0", 0),
        ("divide", "0", "5", 0),
        ("power", "5", "0", 1),
    ],
)
def test_cli_handles_negative_decimal_and_zero_values(
    operation, first, second, expected
):
    result = run_cli(operation, first, second)

    assert result.returncode == 0
    assert float(result.stdout) == pytest.approx(expected)
    assert result.stderr == ""


def test_cli_help_succeeds():
    result = run_cli("--help")

    assert result.returncode == 0
    assert "usage:" in result.stdout.lower()
    for operation in ("add", "subtract", "multiply", "divide", "power"):
        assert operation in result.stdout
    assert result.stderr == ""


@pytest.mark.parametrize(
    "arguments",
    [
        (),
        ("add", "1"),
        ("add",),
        ("unknown", "1", "2"),
        ("add", "one", "2"),
        ("add", "1", "two"),
    ],
)
def test_cli_rejects_invalid_usage(arguments):
    result = run_cli(*arguments)

    assert result.returncode == 2
    assert result.stdout == ""
    assert result.stderr
    assert "usage:" in result.stderr.lower()
    assert "Traceback" not in result.stderr


@pytest.mark.parametrize(
    ("operation", "first", "second", "message"),
    [
        ("divide", "10", "0", "Cannot divide by zero."),
        ("divide", "0", "0", "Cannot divide by zero."),
        ("divide", "-10", "0", "Cannot divide by zero."),
        ("power", "0", "-1", "zero to a negative power"),
        ("power", "2", "0.5", "exponent must be an integer"),
    ],
)
def test_cli_reports_calculation_errors(operation, first, second, message):
    result = run_cli(operation, first, second)

    assert result.returncode == 1
    assert result.stdout == ""
    assert message in result.stderr
    assert "Traceback" not in result.stderr


@pytest.mark.parametrize(
    ("first", "second"),
    [("10", "0"), ("0", "0"), ("-10", "0")],
)
def test_cli_division_by_zero_has_one_user_facing_error(first, second):
    result = run_cli("divide", first, second)

    assert result.returncode == 1
    assert result.stdout == ""
    assert result.stderr == "calculation error: Cannot divide by zero.\n"
