"""enumerate() — Adding index counters to iterables.

Difficulty: 🟢 Easy
Topics: enumerate(), for loop, unpacking, start parameter, dict building

enumerate(iterable, start=0) returns an iterator of (index, element) pairs.
It replaces the anti-pattern of manually tracking indices with a counter.

Author: @rampal-punia
"""


def basic_enumerate() -> None:
    """Show basic enumerate usage with default and custom start."""
    languages = ["Python", "Rust", "JavaScript"]

    # Default: index starts from 0
    print("── Default start=0 ──")
    for index, lang in enumerate(languages):
        print(f"  {index=}, {lang=}")

    # Custom start
    print("\n── Custom start=1001 ──")
    for index, lang in enumerate(languages, start=1001):
        print(f"  {index=}, {lang=}")


def enumerate_with_strings() -> None:
    """Enumerate over characters in a string."""
    print("\n── Enumerate over a string ──")
    for i, char in enumerate("Python"):
        print(f"  [{i}] '{char}'")


def enumerate_to_dict() -> None:
    """Build a dictionary from enumerate (index → value mapping)."""
    print("\n── Build dict from enumerate ──")
    fruits = ["apple", "banana", "cherry"]
    fruit_dict = dict(enumerate(fruits, start=1))
    print(f"  {fruit_dict}")  # {1: 'apple', 2: 'banana', 3: 'cherry'}


def enumerate_with_unpacking() -> None:
    """Enumerate over a list of tuples with nested unpacking."""
    print("\n── Enumerate + nested unpacking ──")
    coordinates = [(10, 20), (30, 40), (50, 60)]
    for i, (x, y) in enumerate(coordinates):
        print(f"  Point {i}: x={x}, y={y}")


def anti_pattern_comparison() -> None:
    """Show why enumerate is better than manual index tracking."""
    print("\n── Anti-pattern vs enumerate ──")
    colors = ["red", "green", "blue"]

    # ❌ Don't do this:
    print("  Manual index (anti-pattern):")
    i = 0
    for color in colors:
        print(f"    {i}: {color}")
        i += 1

    # ✅ Do this instead:
    print("  With enumerate (Pythonic):")
    for i, color in enumerate(colors):
        print(f"    {i}: {color}")


if __name__ == "__main__":
    basic_enumerate()
    enumerate_with_strings()
    enumerate_to_dict()
    enumerate_with_unpacking()
    anti_pattern_comparison()

# For more on Python follow: https://x.com/rs_punia_
