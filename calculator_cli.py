"""Command-line interface for the calculator."""

import argparse
import logging
import sys

from calculator import add, divide, multiply, power, subtract


OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
}


def _suppress_default_calculator_logging() -> None:
    """Keep the CLI error output clear unless logging was configured."""
    calculator_logger = logging.getLogger("calculator")
    root_logger = logging.getLogger()

    if not calculator_logger.handlers and not root_logger.handlers:
        calculator_logger.addHandler(logging.NullHandler())
        calculator_logger.propagate = False


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the calculator CLI."""
    parser = argparse.ArgumentParser(
        description="Perform a calculation with two numbers."
    )
    parser.add_argument("operation", choices=OPERATIONS)
    parser.add_argument("number1", type=float)
    parser.add_argument("number2", type=float)
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the calculator CLI and return its process exit code."""
    _suppress_default_calculator_logging()
    args = build_parser().parse_args(argv)
    operation = OPERATIONS[args.operation]
    second_number = args.number2

    if operation is power:
        if not second_number.is_integer():
            print(
                "calculation error: power exponent must be an integer.",
                file=sys.stderr,
            )
            return 1
        second_number = int(second_number)

    try:
        result = operation(args.number1, second_number)
    except (OverflowError, ValueError, ZeroDivisionError) as error:
        print(f"calculation error: {error}", file=sys.stderr)
        return 1

    print(result)
    return 0
