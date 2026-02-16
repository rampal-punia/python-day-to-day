"""yield vs append — Two ways to build collections, compared.

Difficulty: 🟡 Intermediate
Topics: yield, generators, list.append(), performance, sys.getsizeof

When building a list of transformed items, you can either:
    1. Append to a list inside a function, then return it
    2. Yield items one at a time from a generator function

When to use which:
    - append: When you need random access to all items at once
    - yield:  When you process items one at a time (streaming/pipes)

Author: @rampal-punia
"""

import sys
import time


def squares_with_append(n: int) -> list[int]:
    """Build a list of squares by appending (eager evaluation)."""
    result: list[int] = []
    for i in range(n):
        result.append(i * i)
    return result


def squares_with_yield(n: int):
    """Yield squares one at a time (lazy evaluation)."""
    for i in range(n):
        yield i * i


if __name__ == "__main__":
    N = 1_000_000

    # ── Correctness: both produce the same values ──
    print("── Correctness Check (first 10) ──")
    appended = squares_with_append(10)
    yielded = list(squares_with_yield(10))
    print(f"  Append: {appended}")
    print(f"  Yield:  {yielded}")
    assert appended == yielded, "Results should be identical"
    print("  ✅ Both produce identical output.\n")

    # ── Memory comparison ──
    print(f"── Memory Comparison (n={N:,}) ──")
    list_result = squares_with_append(N)
    gen_result = squares_with_yield(N)
    print(f"  List (append):     {sys.getsizeof(list_result):>12,} bytes")
    print(f"  Generator (yield): {sys.getsizeof(gen_result):>12,} bytes\n")

    # ── Speed comparison ──
    print(f"── Speed Comparison (n={N:,}) ──")

    start = time.perf_counter()
    _ = squares_with_append(N)
    append_time = time.perf_counter() - start
    print(f"  Append time:  {append_time:.4f}s")

    start = time.perf_counter()
    _ = list(squares_with_yield(N))  # Force full evaluation for fair comparison
    yield_time = time.perf_counter() - start
    print(f"  Yield time:   {yield_time:.4f}s")

    # ── Key insight ──
    print("\n── Key Insight ──")
    print("  yield shines when you DON'T need all items:")
    start = time.perf_counter()
    gen = squares_with_yield(N)
    first_five = [next(gen) for _ in range(5)]
    partial_time = time.perf_counter() - start
    print(f"  First 5 from generator: {first_five}  ({partial_time:.6f}s)")

# For more on Python follow: https://x.com/rs_punia_
