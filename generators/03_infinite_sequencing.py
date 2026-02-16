"""Generators 03 — Infinite sequences.

Difficulty: 🟡 Intermediate
Topics: infinite generators, while True + yield, Fibonacci, natural numbers

Generators are perfect for infinite sequences because they only compute
the next value when asked. You can't store infinity in a list, but you
CAN yield infinity one item at a time.

Author: @rampal-punia
"""

from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    """Yield the infinite Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...

    Each value is the sum of the two preceding values.
    This generator never terminates — use `break` or `islice` to stop.

    Yields:
        The next Fibonacci number.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def natural_numbers(start: int = 1) -> Generator[int, None, None]:
    """Yield an infinite sequence of natural numbers.

    Args:
        start: The first number to yield (default: 1).

    Yields:
        Consecutive integers starting from `start`.
    """
    n = start
    while True:
        yield n
        n += 1


def powers_of_two() -> Generator[int, None, None]:
    """Yield infinite powers of 2: 1, 2, 4, 8, 16, ...

    Yields:
        The next power of 2.
    """
    n = 1
    while True:
        yield n
        n *= 2


if __name__ == "__main__":
    # ── Fibonacci: first 10 numbers ──
    print("── First 15 Fibonacci numbers ──")
    fib = fibonacci()
    first_15 = [next(fib) for _ in range(15)]
    print(f"  {first_15}")

    # ── Fibonacci: numbers in a range ──
    print("\n── Fibonacci numbers between 100 and 1000 ──")
    fib = fibonacci()
    in_range = []
    for f in fib:
        if f > 1000:
            break
        if f >= 100:
            in_range.append(f)
    print(f"  {in_range}")

    # ── Natural numbers ──
    print("\n── First 10 natural numbers ──")
    nat = natural_numbers()
    print(f"  {[next(nat) for _ in range(10)]}")

    # ── Powers of two ──
    print("\n── First 10 powers of 2 ──")
    pows = powers_of_two()
    print(f"  {[next(pows) for _ in range(10)]}")
