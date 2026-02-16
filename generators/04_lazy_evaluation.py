"""Generators 04 — Lazy evaluation: compute only what you need.

Difficulty: 🟡 Intermediate
Topics: lazy vs eager evaluation, performance comparison, prime numbers

Lazy evaluation means values are computed ON DEMAND, not upfront.
A list eagerly computes ALL values before you can access any.
A generator lazily computes each value only when you ask for it.

This matters when:
    - You only need the first few results from a large computation
    - The dataset is too large to fit in memory
    - Computations are expensive and you might stop early

Author: @rampal-punia
"""

import sys
import time
from typing import Generator


def is_prime(n: int) -> bool:
    """Check if a number is prime using trial division.

    Args:
        n: The number to test.

    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_list(n: int) -> list[int]:
    """Return ALL primes below n as a list (eager — computes everything upfront)."""
    return [x for x in range(2, n) if is_prime(x)]


def prime_generator(n: int) -> Generator[int, None, None]:
    """Yield primes below n one at a time (lazy — computes on demand)."""
    for x in range(2, n):
        if is_prime(x):
            yield x


if __name__ == "__main__":
    N = 500_000
    FIRST_K = 10

    # ── Eager: list builds ALL primes first, then you pick 10 ──
    print(f"── Finding first {FIRST_K} primes below {N:,} ──\n")

    start = time.perf_counter()
    all_primes = prime_list(N)
    list_time = time.perf_counter() - start
    print(f"  List (eager):      {all_primes[:FIRST_K]}")
    print(f"  Time:              {list_time:.4f}s")
    print(f"  Memory:            {sys.getsizeof(all_primes):,} bytes")
    print(f"  Total computed:    {len(all_primes):,} primes\n")

    # ── Lazy: generator computes only 10 primes, then stops ──
    start = time.perf_counter()
    gen = prime_generator(N)
    first_ten = [next(gen) for _ in range(FIRST_K)]
    gen_time = time.perf_counter() - start
    print(f"  Generator (lazy):  {first_ten}")
    print(f"  Time:              {gen_time:.4f}s")
    print(f"  Memory:            {sys.getsizeof(gen):,} bytes")
    print(f"  Total computed:    {FIRST_K} primes (only what we asked for)")

    # ── Summary ──
    if list_time > 0 and gen_time > 0:
        speedup = list_time / gen_time
        print(f"\n  ⚡ Generator was ~{speedup:.0f}x faster for first {FIRST_K} items!")
