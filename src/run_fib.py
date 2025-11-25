"""Small CLI for the Fibonacci functions in `fibonacci.py`.

Usage examples:
    python -m src.run_fib 10        # prints fib(10)
    python -m src.run_fib 10 --seq  # prints first 10 numbers
    python -m src.run_fib 10 --recursive  # use recursive implementation
"""
import argparse
from .fibonacci import fib, fib_recursive, fib_sequence


def main() -> None:
    parser = argparse.ArgumentParser(description="Fibonacci CLI")
    parser.add_argument("n", type=int, help="Index or length (non-negative integer)")
    parser.add_argument("--seq", action="store_true", help="Print first n Fibonacci numbers")
    parser.add_argument("--recursive", action="store_true", help="Use recursive implementation for single value")

    args = parser.parse_args()
    n = args.n

    if args.seq:
        seq = fib_sequence(n)
        print(seq)
    else:
        if args.recursive:
            print(fib_recursive(n))
        else:
            print(fib(n))


if __name__ == "__main__":
    main()
