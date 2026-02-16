"""List vs Generator — Understanding yield in functions.

Difficulty: 🟢 Easy
Topics: yield, generator function, lazy evaluation, memory efficiency

A function with `yield` returns a generator object instead of a list.
Values are produced one at a time (lazy), saving memory.

Author: @rampal-punia
"""

import sys
from collections.abc import Generator


def my_generator(n: int) -> Generator[int, None, None]:
    """Yield integers from 0 to n-1."""
    for i in range(n):
        yield i


def my_list_builder(n: int) -> list[int]:
    """Return a list of integers from 0 to n-1."""
    return list(range(n))


if __name__ == "__main__":
    n = 10_000

    gen = my_generator(n)
    lst = my_list_builder(n)

    print("── Generator vs List ──")
    print(f"  Generator type:  {type(gen)}")
    print(f"  List type:       {type(lst)}")
    print(f"  Generator size:  {sys.getsizeof(gen):>8} bytes")
    print(f"  List size:       {sys.getsizeof(lst):>8} bytes")

    # Iterating a generator
    print("\n── First 10 values from generator ──")
    small_gen = my_generator(10)
    for val in small_gen:
        print(f"  {val}", end="")
    print()

    # Generator is exhausted after one pass
    print(f"\n  Remaining after loop: {list(small_gen)}")  # []
