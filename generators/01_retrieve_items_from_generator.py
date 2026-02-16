"""Generators 01 — Retrieving items from a generator.

Difficulty: 🟢 Easy
Topics: next(), __next__(), StopIteration, for-loop, generator exhaustion

There are 3 ways to pull values from a generator:
    1. next(gen)          — preferred, built-in function
    2. gen.__next__()     — dunder method (same thing under the hood)
    3. for item in gen:   — cleanest, handles StopIteration automatically

Key insight: A generator can only be consumed ONCE. After exhaustion,
you need to create a new generator object.

Author: @rampal-punia
"""

from typing import Generator


def counting_generator(n: int) -> Generator[int, None, None]:
    """Yield integers from 0 to n-1.

    Args:
        n: Upper limit (exclusive).

    Yields:
        Integers from 0 to n-1, one at a time.
    """
    for i in range(n):
        yield i


def simple_generator() -> Generator[int, None, None]:
    """A minimal generator yielding 3 fixed values."""
    yield 1
    yield 2
    yield 3


if __name__ == "__main__":
    # ── Method 1: next() built-in function (preferred) ──
    print("── Method 1: next() ──")
    gen = counting_generator(5)
    print(f"  next(gen) → {next(gen)}")  # 0
    print(f"  next(gen) → {next(gen)}")  # 1
    print(f"  next(gen) → {next(gen)}")  # 2

    # ── Method 2: __next__() dunder method ──
    print("\n── Method 2: __next__() ──")
    print(f"  gen.__next__() → {gen.__next__()}")  # 3
    print(f"  gen.__next__() → {gen.__next__()}")  # 4

    # ── Handling StopIteration ──
    print("\n── StopIteration Handling ──")
    try:
        next(gen)  # Generator exhausted!
    except StopIteration:
        print("  Caught StopIteration — generator is exhausted.")

    # ── Method 3: for-loop (handles StopIteration automatically) ──
    print("\n── Method 3: for-loop ──")
    gen = simple_generator()  # New generator — old one was consumed!
    for value in gen:
        print(f"  {value}")

    # Prove it's exhausted after the for-loop
    remaining = list(gen)
    print(f"  Remaining after for-loop: {remaining}  (empty = exhausted)")

    # ── next() with default value (avoids StopIteration) ──
    print("\n── next() with default value ──")
    gen = simple_generator()
    for _ in range(5):  # Ask for 5, but only 3 exist
        value = next(gen, "DONE")
        print(f"  next(gen, 'DONE') → {value}")
