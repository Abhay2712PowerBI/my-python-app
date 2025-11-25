import pytest

from src import fibonacci


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55)])
def test_fib_iterative(n, expected):
    assert fibonacci.fib(n) == expected


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (5, 5), (8, 21)])
def test_fib_recursive(n, expected):
    assert fibonacci.fib_recursive(n) == expected


def test_sequence_length_and_values():
    seq = fibonacci.fib_sequence(6)
    assert seq == [0, 1, 1, 2, 3, 5]


def test_generator_matches_sequence():
    gen = list(fibonacci.fib_generator(7))
    assert gen == fibonacci.fib_sequence(7)


def test_negative_raises():
    with pytest.raises(ValueError):
        fibonacci.fib(-1)
