"""Prime Check — Method 2: One-liner with all().

Difficulty: 🟡 Intermediate
Topics: all(), generator expression, functional style

all(n % i for i in range(2, √n+1)) returns True if NONE
of the divisions have zero remainder → meaning n is prime.

Author: @rampal-punia
"""


def is_prime(n: int) -> bool:
    """Check primality using all() with a generator expression.

    This is a Pythonic one-liner approach. Short-circuits on
    the first divisor found (generator is lazy).

    Args:
        n: The integer to test.

    Returns:
        True if n is prime.
    """
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))


if __name__ == "__main__":
    print("── Prime Check (all + generator) ──")
    test_values = [0, 1, 2, 3, 4, 17, 22, 97, 100]
    for n in test_values:
        print(f"  {n:>4} → {'Prime' if is_prime(n) else 'Not prime'}")

# For more on Python follow: https://x.com/rs_punia_
