"""Prime Range — Find all primes in a given range.

Difficulty: 🟡 Intermediate
Topics: list comprehension, all(), prime range, generator pipeline

Author: @rampal-punia
"""


def primes_in_range(start: int, end: int) -> list[int]:
    """Find all prime numbers in [start, end) using list comprehension.

    Args:
        start: Start of range (inclusive).
        end: End of range (exclusive).

    Returns:
        List of prime numbers in the range.
    """
    return [
        x
        for x in range(max(2, start), end)
        if all(x % y != 0 for y in range(2, int(x**0.5) + 1))
    ]


if __name__ == "__main__":
    print("── Primes in Range ──")
    start, end = 100, 200
    result = primes_in_range(start, end)
    print(f"  Range: [{start}, {end})")
    print(f"  Count: {len(result)}")
    print(f"  Primes: {result}")

    # Quick summary for a larger range
    big = primes_in_range(1_000, 5_000)
    print(f"\n  Primes in [1000, 5000): {len(big)} primes found")
    print(f"  First 10: {big[:10]}")
    print(f"  Last  10: {big[-10:]}")

# For more on Python follow: https://x.com/rs_punia_
