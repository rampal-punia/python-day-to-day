"""Quiz 15: Identity of equal return values.

Difficulty: 🔴 Advanced
Topics: is vs ==, CPython integer caching, identity, set

Question: What do `func1 is func2` and `len(my_strange_set)` output?
    A) True, 1
    B) False, 2
    C) Implementation-dependent
"""


def add_number(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def quiz() -> None:
    """CPython caches small integers (-5 to 256), so `is` may be True."""
    func1 = add_number(4, 5)  # 9
    func2 = add_number(4, 5)  # 9

    print("── Quiz 15 ──")
    print(f"  func1 = add_number(4, 5) = {func1}")
    print(f"  func2 = add_number(4, 5) = {func2}")
    print(f"  func1 is func2:    {func1 is func2}")
    print(f"  func1 == func2:    {func1 == func2}")

    my_strange_set = {func1, func2}
    print(f"  len({{func1, func2}}): {len(my_strange_set)}")

    # Answer (CPython): True, 1
    # CPython caches integers from -5 to 256. Since 9 is in
    # that range, both func1 and func2 point to the SAME object.
    # So `is` returns True and the set has only 1 element.
    #
    # WARNING: This is an implementation detail! Values > 256
    # may NOT be cached:
    big1 = add_number(200, 200)  # 400
    big2 = add_number(200, 200)  # 400
    print(f"\n  big1 = 400, big2 = 400")
    print(f"  big1 is big2: {big1 is big2}  (may be False!)")
    print(f"  big1 == big2: {big1 == big2}  (always True)")


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
