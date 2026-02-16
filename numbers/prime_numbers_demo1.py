"""Prime Check — Method 1: Loop with sqrt optimization.

Difficulty: 🟢 Easy
Topics: primality test, sqrt optimization, range()

Why sqrt? If n = a × b, then min(a, b) ≤ √n.
So we only need to check divisors up to √n.

Author: @rampal-punia
"""


def is_prime(n: int) -> bool:
    """Check if a number is prime using trial division up to √n.

    Args:
        n: The integer to test.

    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("── Prime Check (Loop) ──")
    test_values = [0, 1, 2, 3, 4, 17, 22, 97, 100]
    for n in test_values:
        print(f"  {n:>4} → {'Prime' if is_prime(n) else 'Not prime'}")

# For more on Python follow: https://x.com/rs_punia_
