"""
Lambda, Map, Filter, Reduce — Functional Programming in Python
================================================================
Higher-order functions and anonymous functions explained with examples.

Author: @rampal-punia
"""

from functools import reduce
from typing import Callable


# ─────────────────────────────────────────────────
# 1. LAMBDA — Anonymous (Inline) Functions
# ─────────────────────────────────────────────────

# Syntax: lambda arguments: expression

square = lambda x: x**2  # single arg
multiply = lambda x, y: x * y  # multiple args
full_name = lambda first, last: f"{first} {last}"  # string ops
is_even = lambda n: n % 2 == 0  # returns bool


# ─────────────────────────────────────────────────
# 2. MAP — Apply function to every item
# ─────────────────────────────────────────────────
# map(function, iterable) → iterator


def demo_map():
    """Transform data without explicit loops."""
    numbers = [1, 2, 3, 4, 5]

    # Lambda with map
    squared = list(map(lambda x: x**2, numbers))
    print(f"  Squared     : {squared}")  # [1, 4, 9, 16, 25]

    # Named function with map
    celsius = [0, 20, 37, 100]
    to_fahrenheit = lambda c: round(c * 9 / 5 + 32, 1)
    fahrenheit = list(map(to_fahrenheit, celsius))
    print(f"  Fahrenheit  : {fahrenheit}")  # [32.0, 68.0, 98.6, 212.0]

    # Map with multiple iterables
    a = [1, 2, 3]
    b = [10, 20, 30]
    sums = list(map(lambda x, y: x + y, a, b))
    print(f"  Pairwise sum: {sums}")  # [11, 22, 33]

    # Map with str methods (no lambda needed!)
    words = ["hello", "WORLD", "PyThOn"]
    titled = list(map(str.title, words))
    print(f"  Titled      : {titled}")  # ['Hello', 'World', 'Python']


# ─────────────────────────────────────────────────
# 3. FILTER — Select items matching a condition
# ─────────────────────────────────────────────────
# filter(function, iterable) → iterator


def demo_filter():
    """Keep only items that satisfy a condition."""
    numbers = range(-5, 6)

    # Filter positive numbers
    positives = list(filter(lambda x: x > 0, numbers))
    print(f"  Positive    : {positives}")  # [1, 2, 3, 4, 5]

    # Filter even numbers
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"  Even        : {evens}")  # [-4, -2, 0, 2, 4]

    # Filter with None removes falsy values
    mixed = [0, 1, "", "hello", None, 42, [], [1, 2], False, True]
    truthy = list(filter(None, mixed))
    print(f"  Truthy only : {truthy}")  # [1, 'hello', 42, [1, 2], True]

    # Real-world: Filter valid emails
    emails = ["user@mail.com", "invalid", "a@b.co", "", "test@test.org"]
    valid = list(filter(lambda e: "@" in e and "." in e, emails))
    print(f"  Valid emails: {valid}")


# ─────────────────────────────────────────────────
# 4. REDUCE — Accumulate to a single value
# ─────────────────────────────────────────────────
# reduce(function, iterable[, initializer]) → value


def demo_reduce():
    """Reduce a sequence to a single value by cumulative application."""
    numbers = [1, 2, 3, 4, 5]

    # Sum (equivalent to sum())
    total = reduce(lambda acc, x: acc + x, numbers)
    print(f"  Sum         : {total}")  # 15

    # Product (equivalent to math.prod())
    product = reduce(lambda acc, x: acc * x, numbers)
    print(f"  Product     : {product}")  # 120

    # Max (equivalent to max())
    maximum = reduce(lambda a, b: a if a > b else b, numbers)
    print(f"  Max         : {maximum}")  # 5

    # Flatten nested lists
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = reduce(lambda acc, lst: acc + lst, nested, [])
    print(f"  Flattened   : {flat}")  # [1, 2, 3, 4, 5, 6]

    # Build string from parts
    words = ["Python", "is", "amazing"]
    sentence = reduce(lambda a, b: f"{a} {b}", words)
    print(f"  Sentence    : {sentence}")  # "Python is amazing"


# ─────────────────────────────────────────────────
# 5. CHAINING — Combining map, filter, reduce
# ─────────────────────────────────────────────────


def demo_chaining():
    """
    Task: From a list of product prices, apply 10% discount to items
    over $50, then compute the total.
    """
    prices = [25.0, 89.99, 45.0, 120.0, 15.0, 78.50, 200.0]

    # Functional approach
    total = reduce(
        lambda acc, p: acc + p,  # step 3: sum
        map(
            lambda p: round(p * 0.9, 2),  # step 2: 10% discount
            filter(lambda p: p > 50, prices),  # step 1: filter > $50
        ),
        0.0,  # initial value
    )
    print(f"  Discounted total: ${total:.2f}")

    # Compare with comprehension (more Pythonic)
    total_v2 = sum(round(p * 0.9, 2) for p in prices if p > 50)
    print(f"  Comprehension  : ${total_v2:.2f}")  # Same result!


# ─────────────────────────────────────────────────
# 6. LAMBDA vs COMPREHENSION — When to Use What
# ─────────────────────────────────────────────────


def demo_comparison():
    """
    Guideline:
    ┌───────────────────┬─────────────────────────────────┐
    │ Use Lambda+Map    │ Simple transforms, method refs  │
    │ Use Comprehension │ Complex logic, readability      │
    │ Use Filter        │ Simple predicates               │
    │ Use Reduce        │ Aggregation to single value     │
    └───────────────────┴─────────────────────────────────┘
    """
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # ❌ Hard to read
    result1 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, data)))

    # ✅ More Pythonic
    result2 = [x**2 for x in data if x % 2 == 0]

    print(f"  map+filter      : {result1}")
    print(f"  comprehension   : {result2}")
    print(f"  Same result?    : {result1 == result2}")  # True


# ─────────────────────────────────────────────────
# 7. SORTING WITH LAMBDA — Extremely Common Pattern
# ─────────────────────────────────────────────────


def demo_sorting_with_lambda():
    """Lambda is THE go-to for custom sort keys."""
    students = [
        {"name": "Alice", "grade": 88, "age": 22},
        {"name": "Bob", "grade": 95, "age": 20},
        {"name": "Charlie", "grade": 88, "age": 21},
        {"name": "Diana", "grade": 92, "age": 23},
    ]

    # Sort by grade (descending), then name (ascending)
    sorted_students = sorted(students, key=lambda s: (-s["grade"], s["name"]))

    print("  Sorted by grade ↓, name ↑:")
    for s in sorted_students:
        print(f"    {s['name']:>8} — Grade: {s['grade']}, Age: {s['age']}")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("1. Lambda Basics")
    print("=" * 55)
    print(f"  square(5)     = {square(5)}")
    print(f"  multiply(3,4) = {multiply(3, 4)}")
    print(f"  full_name     = {full_name('Guido', 'van Rossum')}")
    print(f"  is_even(7)    = {is_even(7)}")

    print("\n" + "=" * 55)
    print("2. Map")
    print("=" * 55)
    demo_map()

    print("\n" + "=" * 55)
    print("3. Filter")
    print("=" * 55)
    demo_filter()

    print("\n" + "=" * 55)
    print("4. Reduce")
    print("=" * 55)
    demo_reduce()

    print("\n" + "=" * 55)
    print("5. Chaining — map + filter + reduce")
    print("=" * 55)
    demo_chaining()

    print("\n" + "=" * 55)
    print("6. Lambda vs Comprehension")
    print("=" * 55)
    demo_comparison()

    print("\n" + "=" * 55)
    print("7. Sorting with Lambda")
    print("=" * 55)
    demo_sorting_with_lambda()
