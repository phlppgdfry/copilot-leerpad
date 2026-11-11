import logging

import pytest

from calculator import add, divide, multiply, percentage, power, subtract


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (2, 3, 5),
        (-2, -3, -5),
        (0, 7, 7),
        (0.1, 0.2, 0.3),
        (2, 0.5, 2.5),
    ],
)
def test_add_returns_sum(first, second, expected):
    """Verify addition with positive, negative, zero, and float inputs."""
    result = add(first, second)

    assert result == pytest.approx(expected)


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (8, 3, 5),
        (3, 8, -5),
        (0, 4, -4),
        (5.5, 2, 3.5),
        (0.3, 0.1, 0.2),
    ],
)
def test_subtract_returns_difference(first, second, expected):
    """Verify subtraction, including negative results and zero."""
    assert subtract(first, second) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (4, 3, 12),
        (-4, 3, -12),
        (9, 0, 0),
        (2.5, 4, 10),
    ],
)
def test_multiply_returns_product(first, second, expected):
    """Verify multiplication with positive, negative, and zero inputs."""
    assert multiply(first, second) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (12, 3, 4),
        (-12, 3, -4),
        (1, 4, 0.25),
        (5, 2.0, 2.5),
        (0, 5, 0),
    ],
)
def test_divide_returns_quotient(first, second, expected):
    """Verify normal, negative, and floating-point division."""
    assert divide(first, second) == pytest.approx(expected)


def test_divide_logs_success(caplog):
    """Verify that a successful division is logged at debug level."""
    with caplog.at_level("DEBUG"):
        divide(10, 2)

    records = [
        record
        for record in caplog.records
        if record.getMessage() == "Division completed successfully."
    ]

    assert len(records) == 1
    assert records[0].levelno == logging.DEBUG


def test_divide_by_zero_raises_zero_division_error():
    """Verify that division by zero raises the expected exception."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_divide_by_zero_logs_error(caplog):
    """Verify that division by zero is logged as an error."""
    with caplog.at_level("ERROR"), pytest.raises(ZeroDivisionError):
        divide(10, 0)

    records = [
        record
        for record in caplog.records
        if record.getMessage() == "Division by zero attempted."
    ]

    assert len(records) == 1
    assert records[0].levelno == logging.ERROR


@pytest.mark.parametrize(
    ("base", "exponent", "expected"),
    [
        (2, 3, 8),
        (2, -3, 0.125),
        (5, 0, 1),
        (-2, 3, -8),
        (2.5, 2, 6.25),
    ],
)
def test_power_returns_raised_value(base, exponent, expected):
    """Verify positive, negative, zero, and floating-point powers."""
    assert power(base, exponent) == pytest.approx(expected)


def test_power_zero_to_negative_exponent_raises_zero_division_error():
    """Verify that zero raised to a negative exponent raises an error."""
    with pytest.raises(ZeroDivisionError):
        power(0, -1)


@pytest.mark.parametrize(
    ("value", "total", "expected"),
    [
        (25, 200, 12.5),
        (50, 100, 50.0),
        (0, 100, 0.0),
        (-25, 100, -25.0),
        (12.5, 50, 25.0),
        (1, 2.0, 50.0),
    ],
)
def test_percentage_returns_percentage(value, total, expected):
    """Verify percentage calculations with integer and float inputs."""
    assert percentage(value, total) == pytest.approx(expected)


def test_percentage_with_zero_total_raises_zero_division_error():
    """Verify that a zero total raises the expected exception."""
    with pytest.raises(ZeroDivisionError):
        percentage(10, 0)