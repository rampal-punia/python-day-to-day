"""String Length Without len() — Multiple approaches to count characters.

Difficulty: 🟢 Easy
Topics: iteration, recursion, reduce, sum with generator, len()

While len() is the standard way, understanding alternatives teaches
fundamental concepts like iteration, recursion, and functional programming.

Author: @rampal-punia
"""

from functools import reduce


# ── Method 1: Manual counter loop ──


def string_length_loop(text: str) -> int:
    """Count characters using a for-loop counter."""
    length = 0
    for _ in text:
        length += 1
    return length


# ── Method 2: sum() with generator ──


def string_length_sum(text: str) -> int:
    """Count characters using sum() with a generator expression."""
    return sum(1 for _ in text)


# ── Method 3: Recursion ──


def string_length_recursive(text: str) -> int:
    """Count characters recursively (for educational purposes)."""
    if text == "":
        return 0
    return 1 + string_length_recursive(text[1:])


# ── Method 4: functools.reduce ──


def string_length_reduce(text: str) -> int:
    """Count characters using functools.reduce."""
    return reduce(lambda count, _: count + 1, text, 0)


if __name__ == "__main__":
    test_string = "Hello, World! 🌍"

    print(f"  String: '{test_string}'\n")
    print(f"  len() (built-in):   {len(test_string)}")
    print(f"  Loop counter:       {string_length_loop(test_string)}")
    print(f"  sum() + generator:  {string_length_sum(test_string)}")
    print(f"  Recursive:          {string_length_recursive(test_string)}")
    print(f"  functools.reduce:   {string_length_reduce(test_string)}")

    # Verify all methods agree
    expected = len(test_string)
    assert all(
        fn(test_string) == expected
        for fn in [
            string_length_loop,
            string_length_sum,
            string_length_recursive,
            string_length_reduce,
        ]
    ), "All methods should produce the same result!"
    print("\n  ✅ All methods produce the same result.")
