import pytest

from calculator import add, divide, multiply, subtract


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (2, 3, 5),
        (-2, -3, -5),
        (0, 7, 7),
        (0.1, 0.2, 0.3),
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
    ],
)
def test_divide_returns_quotient(first, second, expected):
    """Verify normal, negative, and floating-point division."""
    assert divide(first, second) == pytest.approx(expected)


def test_divide_by_zero_raises_zero_division_error():
    """Verify that division by zero raises the expected exception."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)