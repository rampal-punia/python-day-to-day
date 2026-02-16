"""FizzBuzz — 5 different approaches from beginner to advanced.

Difficulty: 🟢 Easy → 🟡 Intermediate → 🔴 Advanced
Topics: if/elif/else, list comprehension, lambda, generators, match/case

The classic FizzBuzz problem:
    For numbers 1 to n, print:
    - "FizzBuzz" if divisible by both 3 and 5
    - "Fizz"     if divisible by 3 only
    - "Buzz"     if divisible by 5 only
    - The number itself otherwise

Author: @rampal-punia
"""

from typing import Generator


# ── 🟢 Method 1: Classic if/elif/else ───────────────────────────────


def fizzbuzz_classic(n: int) -> list[str]:
    """Solve FizzBuzz using straightforward conditionals.

    Args:
        n: Upper limit (inclusive).

    Returns:
        List of FizzBuzz results.
    """
    results: list[str] = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(number))
    return results


# ── 🟡 Method 2: List Comprehension (one-liner) ────────────────────


def fizzbuzz_comprehension(n: int) -> list[str]:
    """Solve FizzBuzz with a list comprehension.

    A concise but still readable single-expression approach.
    """
    return [
        (
            "FizzBuzz"
            if i % 15 == 0
            else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)
        )
        for i in range(1, n + 1)
    ]


# ── 🟡 Method 3: Lambda + map ──────────────────────────────────────


def fizzbuzz_lambda(n: int) -> list[str]:
    """Solve FizzBuzz using a lambda mapped over a range."""
    fb = lambda x: (
        "FizzBuzz"
        if x % 15 == 0
        else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else str(x)
    )
    return list(map(fb, range(1, n + 1)))


# ── 🔴 Method 4: Generator (memory-efficient) ──────────────────────


def fizzbuzz_generator(n: int) -> Generator[str, None, None]:
    """Solve FizzBuzz lazily with a generator.

    Yields one result at a time — ideal for very large ranges.

    Yields:
        The FizzBuzz string for each number 1 to n.
    """
    for i in range(1, n + 1):
        yield (
            "FizzBuzz"
            if i % 15 == 0
            else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)
        )


# ── 🔴 Method 5: String Concatenation (no hardcoded "FizzBuzz") ────


def fizzbuzz_concat(n: int) -> list[str]:
    """Solve FizzBuzz by building the string from parts.

    This approach scales to more divisors (e.g., Fizz/Buzz/Jazz)
    without needing to check every combination explicitly.
    """
    results: list[str] = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        results.append(output or str(i))
    return results


if __name__ == "__main__":
    N = 20

    print("── 🟢 Method 1: Classic if/elif/else ──")
    print(fizzbuzz_classic(N))

    print("\n── 🟡 Method 2: List Comprehension ──")
    print(fizzbuzz_comprehension(N))

    print("\n── 🟡 Method 3: Lambda + map ──")
    print(fizzbuzz_lambda(N))

    print("\n── 🔴 Method 4: Generator ──")
    print(list(fizzbuzz_generator(N)))

    print("\n── 🔴 Method 5: Concat (extensible) ──")
    print(fizzbuzz_concat(N))

    # Verify all methods produce the same result
    assert (
        fizzbuzz_classic(100)
        == fizzbuzz_comprehension(100)
        == fizzbuzz_lambda(100)
        == list(fizzbuzz_generator(100))
        == fizzbuzz_concat(100)
    ), "All methods should produce identical output!"
    print("\n✅ All 5 methods produce identical output for n=100.")

# For more on Python follow: https://x.com/rs_punia_
