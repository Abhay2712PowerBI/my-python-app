from functools import lru_cache
from typing import List, Iterator


def fib(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed).

    fib(0) == 0, fib(1) == 1
    Uses an iterative approach (O(n) time, O(1) memory).
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@lru_cache(maxsize=None)
def fib_recursive(n: int) -> int:
    """Recursive Fibonacci with memoization. Suitable for small n or demonstration."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_sequence(n: int) -> List[int]:
    """Return a list with the first `n` Fibonacci numbers (length n).

    Example: fib_sequence(5) -> [0, 1, 1, 2, 3]
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    seq: List[int] = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def fib_generator(n: int) -> Iterator[int]:
    """Yield the first `n` Fibonacci numbers as a generator."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


__all__ = ["fib", "fib_recursive", "fib_sequence", "fib_generator"]
