"""all() vs any() — Two essential built-in functions for iterables.

Difficulty: 🟢 Easy
Topics: all(), any(), truthiness, falsy values, short-circuit evaluation

Quick Reference:
    all(iterable) → True if EVERY element is truthy (or iterable is empty)
    any(iterable) → True if ANY element is truthy (False if iterable is empty)

Author: @rampal-punia
"""


def demo_all() -> None:
    """Demonstrate how all() works with various iterables."""
    print("── all(): True only if ALL elements are truthy ──\n")

    # 0 is falsy → all() returns False
    numbers = [2, 3, 4, 6, 0, 8]
    print(f"  all({numbers})        = {all(numbers)}")  # False (0 is falsy)

    # [], {} are falsy → all() returns False
    mixed = (True, True, [1], [], {})
    print(f"  all({mixed}) = {all(mixed)}")  # False

    # [[]] is truthy! (a non-empty list containing an empty list)
    nested = [True, [1, 2, 3], [[]]]
    print(f"  all({nested})    = {all(nested)}")  # True
    print(f"    Why? bool([[]]) = {bool([[]])}")  # True (non-empty list)

    # Empty iterable → all() returns True (vacuous truth)
    print(f"  all([])                  = {all([])}")  # True


def demo_any() -> None:
    """Demonstrate how any() works with various iterables."""
    print("\n── any(): True if ANY element is truthy ──\n")

    numbers = [2, 3, 4, 6, 0, 8]
    print(f"  any({numbers})        = {any(numbers)}")  # True

    mixed = (True, True, [1], [], {})
    print(f"  any({mixed}) = {any(mixed)}")  # True

    all_truthy = [True, [1, 2, 3], "John"]
    print(f"  any({all_truthy})  = {any(all_truthy)}")  # True

    # Empty iterable → any() returns False
    print(f"  any([])                  = {any([])}")  # False


def demo_practical_uses() -> None:
    """Show practical use cases for all() and any()."""
    print("\n── Practical Examples ──\n")

    # Validate all fields are filled
    form_data = {"name": "Alice", "email": "alice@example.com", "age": 30}
    all_filled = all(form_data.values())
    print(f"  All form fields filled? {all_filled}")  # True

    # Check if any score is above threshold
    scores = [45, 62, 38, 71, 55]
    has_passing = any(s >= 70 for s in scores)
    print(f"  Any score >= 70? {has_passing}")  # True

    # Check if all passwords meet length requirement
    passwords = ["abc", "MyP@ssw0rd", "hi"]
    all_strong = all(len(p) >= 8 for p in passwords)
    print(f"  All passwords >= 8 chars? {all_strong}")  # False


if __name__ == "__main__":
    demo_all()
    demo_any()
    demo_practical_uses()

# For more on Python follow: https://x.com/rs_punia_
