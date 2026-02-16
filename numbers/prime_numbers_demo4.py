"""Prime Range (User Input) — Find primes from user-specified range.

Difficulty: 🟡 Intermediate
Topics: input parsing, map(), validation, prime range

Author: @rampal-punia
"""


def primes_in_range(start: int, end: int) -> list[int]:
    """Find all prime numbers in [start, end).

    Args:
        start: Start of range (inclusive).
        end: End of range (exclusive).

    Returns:
        List of primes in the range.
    """
    return [
        x
        for x in range(max(2, start), end)
        if all(x % y != 0 for y in range(2, int(x**0.5) + 1))
    ]


def main() -> None:
    """Get range from user and display primes."""
    try:
        raw = input("Enter start and end (space-separated, e.g. 1000 5000): ")
        start, end = map(int, raw.split())
        if start >= end:
            print("  Error: start must be less than end.")
            return
    except ValueError:
        print("  Error: please enter two valid integers.")
        return

    result = primes_in_range(start, end)
    print(f"\n  Range: [{start}, {end})")
    print(f"  Found: {len(result)} primes")
    if len(result) <= 50:
        print(f"  Primes: {result}")
    else:
        print(f"  First 10: {result[:10]}")
        print(f"  Last  10: {result[-10:]}")


if __name__ == "__main__":
    main()

# For more on Python follow: https://x.com/rs_punia_
