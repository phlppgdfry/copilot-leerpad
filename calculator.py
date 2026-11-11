def add(first: int | float, second: int | float) -> int | float:
    """Return the sum of two numbers."""
    return first + second


def subtract(first: int | float, second: int | float) -> int | float:
    """Return the difference between two numbers."""
    return first - second


def multiply(first: int | float, second: int | float) -> int | float:
    """Return the product of two numbers."""
    return first * second


def divide(a: int | float, b: int | float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def power(base: int | float, exponent: int) -> int | float:
    """Return the base raised to the given integer exponent."""
    return base**exponent


def percentage(value: int | float, total: int | float) -> float:
    """Return value as a percentage of total."""
    if total == 0:
        raise ZeroDivisionError("Cannot calculate a percentage of zero.")

    return (value / total) * 100