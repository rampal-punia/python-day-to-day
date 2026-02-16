"""List Identity vs Equality & count() — `is` vs `==` for lists.

Difficulty: 🟢 Easy
Topics: list.count(), slicing, identity vs equality, shallow copy

Key insight:
    lst is lst[:]  → False  (slice creates a NEW list object)
    lst == lst[:]  → True   (same values)
    But .count() returns the same result on both!

Author: @rampal-punia
"""


def demo_list_identity_and_count() -> None:
    """Show the difference between list identity and equality."""
    lst = [10, 23, 25, 45, 10]
    sliced = lst[:]  # Shallow copy via slice

    print("── Identity vs Equality ──")
    print(f"  lst          = {lst}")
    print(f"  lst[:]       = {sliced}")
    print(f"  lst is lst[:] : {lst is sliced}")  # False (different objects)
    print(f"  lst == lst[:] : {lst == sliced}")  # True  (same values)

    print("\n── count() Method ──")
    print(f"  lst.count(10)     = {lst.count(10)}")  # 2
    print(f"  lst[:].count(10)  = {sliced.count(10)}")  # 2 (same result)
    print(f"  lst.count(25)     = {lst.count(25)}")  # 1
    print(f"  lst.count(99)     = {lst.count(99)}")  # 0 (not found)


if __name__ == "__main__":
    demo_list_identity_and_count()
