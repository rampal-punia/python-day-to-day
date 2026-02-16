"""Generators 00 — Introduction: What are generators and why use them?

Difficulty: 🟢 Easy
Topics: yield, memory efficiency, generators vs lists, chunked processing

Key takeaway:
    Generators produce values ONE AT A TIME (lazy evaluation) instead of
    building the entire collection in memory. This makes them ideal for
    large datasets, streams, and pipelines.

Author: @rampal-punia
"""

import sys
from typing import Generator


def generate_squares(n: int) -> Generator[int, None, None]:
    """Yield squares of numbers from 0 to n-1.

    Unlike a list comprehension, this only computes one value at a time,
    keeping memory usage constant regardless of `n`.

    Args:
        n: How many squares to generate.

    Yields:
        The square of each integer from 0 to n-1.
    """
    for i in range(n):
        yield i**2


def process_in_chunks(
    gen: Generator[int, None, None], chunk_size: int = 1000
) -> Generator[list[int], None, None]:
    """Consume a generator in fixed-size chunks.

    This is useful for batch processing: reading N records at a time
    from a database, file, or API without loading everything at once.

    Args:
        gen: Any generator of integers.
        chunk_size: Number of items per chunk.

    Yields:
        Lists of up to `chunk_size` items.
    """
    chunk: list[int] = []
    for item in gen:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:  # Don't forget the last partial chunk
        yield chunk


if __name__ == "__main__":
    N = 1_000_000

    # ── Memory comparison ──
    gen = generate_squares(N)
    list_comp = [i**2 for i in range(N)]

    print("── Memory Comparison ──")
    print(f"  Generator object size:  {sys.getsizeof(gen):>10,} bytes")
    print(f"  List (1M items) size:   {sys.getsizeof(list_comp):>10,} bytes")
    print(
        f"  Ratio: list is ~{sys.getsizeof(list_comp) // sys.getsizeof(gen)}x larger\n"
    )

    # ── Chunked processing ──
    print("── Chunked Processing (first 3 chunks of 1000) ──")
    gen = generate_squares(N)
    for i, chunk in enumerate(process_in_chunks(gen, chunk_size=1000)):
        if i >= 3:
            break
        print(
            f"  Chunk {i}: [{chunk[0]}, {chunk[1]}, ... {chunk[-1]}]  (len={len(chunk)})"
        )
