"""Equality vs Identity — `==` vs `is` across data types.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: ==, is, id(), value equality, identity, set ordering

Key insight:
    ==  checks VALUE equality  (do they contain the same data?)
    is  checks IDENTITY        (are they the exact same object in memory?)

Sets are unordered, so {9, 8, 5} == {5, 8, 9} → True.
Lists and tuples ARE ordered, so [9, 8, 5] != [5, 8, 9].

Author: @rampal-punia
"""


def compare_equality_vs_identity() -> None:
    """Demonstrate == vs is for sets, lists, and tuples."""
    print("── Sets (unordered: order doesn't matter for ==) ──")
    s1 = {9, 8, 5}
    s2 = {5, 8, 9}
    print(f"  s1 = {s1},  s2 = {s2}")
    print(f"  s1 == s2:  {s1 == s2}")  # True  (same elements)
    print(f"  s1 is s2:  {s1 is s2}")  # False (different objects)
    print(f"  id(s1)={id(s1)}, id(s2)={id(s2)}")

    print("\n── Lists (ordered: order matters for ==) ──")
    l1 = [9, 8, 5]
    l2 = [5, 8, 9]
    print(f"  l1 = {l1},  l2 = {l2}")
    print(f"  l1 == l2:  {l1 == l2}")  # False (different order)
    print(f"  l1 is l2:  {l1 is l2}")  # False

    print("\n── Tuples (ordered: order matters for ==) ──")
    t1 = (9, 8, 5)
    t2 = (5, 8, 9)
    print(f"  t1 = {t1},  t2 = {t2}")
    print(f"  t1 == t2:  {t1 == t2}")  # False
    print(f"  t1 is t2:  {t1 is t2}")  # False

    # 🟡 Intermediate: Integer caching surprise
    print("\n── Integer Caching (CPython implementation detail) ──")
    a = 256
    b = 256
    print(f"  a=256, b=256 → a is b: {a is b}")  # True (cached: -5 to 256)
    c = 257
    d = 257
    print(f"  c=257, d=257 → c is d: {c is d}")  # May be False outside REPL
    print("  (CPython caches integers from -5 to 256)")


if __name__ == "__main__":
    compare_equality_vs_identity()
