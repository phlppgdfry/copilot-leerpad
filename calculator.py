def add(first: int | float, second: int | float) -> int | float:
    """Return the sum of two numbers."""
    return first + second


def subtract(first: int | float, second: int | float) -> int | float:
    """Return the difference between two numbers."""
    return first - second


def multiply(first: int | float, second: int | float) -> int | float:
    """Return the product of two numbers."""
    return first * second


def divide(first: int | float, second: int | float) -> float:
    """Return the result of dividing the first number by the second."""
    if second == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return first / second