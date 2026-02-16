"""Factorial — 4 different methods to compute n!

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: math.factorial, math.prod, functools.reduce, recursion

Note: numpy.prod overflows for large factorials (returns 0 for 20!).
Use math.factorial or math.prod for arbitrary precision.

Author: @rampal-punia
"""

import math
from functools import reduce


# 🟢 Method 1: math.factorial (recommended)
def factorial_math(n: int) -> int:
    """Compute n! using the built-in math.factorial."""
    return math.factorial(n)


# 🟢 Method 2: math.prod
def factorial_prod(n: int) -> int:
    """Compute n! using math.prod over range(1, n+1)."""
    return math.prod(range(1, n + 1))


# 🟡 Method 3: functools.reduce
def factorial_reduce(n: int) -> int:
    """Compute n! using reduce with a lambda."""
    return reduce(lambda acc, x: acc * x, range(1, n + 1), 1)


# 🟡 Method 4: Recursion
def factorial_recursive(n: int) -> int:
    """Compute n! recursively.

    Args:
        n: Non-negative integer.

    Returns:
        n factorial.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    x = 20
    print(f"── Factorial of {x} ──")
    methods = {
        "math.factorial": factorial_math,
        "math.prod": factorial_prod,
        "reduce": factorial_reduce,
        "recursive": factorial_recursive,
    }
    for name, func in methods.items():
        result = func(x)
        print(f"  {name:<18} = {result}")

    # Verify all methods agree
    results = [func(x) for func in methods.values()]
    assert len(set(results)) == 1, "Methods disagree!"
    print(f"\n  ✅ All 4 methods return the same result.")

# For more on Python follow: https://x.com/rs_punia_
