"""Generators 02 — Pipelining with generators.

Difficulty: 🟡 Intermediate
Topics: generator pipelines, data transformation, lazy composition

Generator pipelining connects multiple generators in series, where each
generator transforms data from the previous one. This is the same pattern
used by Unix pipes (cmd1 | cmd2 | cmd3) and is the foundation of ETL.

Key benefits:
    - Each stage processes ONE item at a time (memory-efficient)
    - Stages are composable and reusable
    - Easy to add/remove/reorder transformation steps

Author: @rampal-punia
"""

from typing import Generator, Iterable


def generate_numbers(n: int) -> Generator[int, None, None]:
    """Stage 1: Produce raw numbers 0 to n-1."""
    for i in range(n):
        yield i


def square(numbers: Iterable[int]) -> Generator[int, None, None]:
    """Stage 2: Square each number."""
    for num in numbers:
        yield num**2


def add_two(numbers: Iterable[int]) -> Generator[int, None, None]:
    """Stage 3: Add 2 to each number."""
    for num in numbers:
        yield num + 2


def filter_even(numbers: Iterable[int]) -> Generator[int, None, None]:
    """Stage 4 (optional): Keep only even numbers."""
    for num in numbers:
        if num % 2 == 0:
            yield num


if __name__ == "__main__":
    n = 10

    # ── Basic pipeline: numbers → square → add_two ──
    print("── Pipeline: generate → square → add_two ──")
    pipeline = add_two(square(generate_numbers(n)))
    result = list(pipeline)
    print(f"  {result}")
    # [2, 3, 6, 11, 18, 27, 38, 51, 66, 83]

    # ── Exhaustion: reusing a consumed pipeline gives nothing ──
    print(f"  Reuse exhausted pipeline: {list(pipeline)}")  # []

    # ── Extended pipeline: add a filter stage ──
    print("\n── Pipeline: generate → square → add_two → filter_even ──")
    pipeline = filter_even(add_two(square(generate_numbers(n))))
    result = list(pipeline)
    print(f"  {result}")
    # [2, 6, 18, 38, 66]

    # ── Visual trace: see what happens at each stage ──
    print("\n── Trace: step-by-step for n=5 ──")
    for i in range(5):
        raw = i
        squared = raw**2
        plus_two = squared + 2
        print(f"  {raw} → square → {squared} → +2 → {plus_two}")
