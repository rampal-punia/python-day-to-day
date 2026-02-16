"""Quiz 16: set.issubset() accepts any iterable.

Difficulty: 🟡 Intermediate
Topics: set.issubset(), iterable arguments, set vs tuple

Question: What is the output of set_a.issubset(tuple_a)?
    A) True
    B) False
    C) Error
"""


def quiz() -> None:
    """issubset() accepts any iterable, not just sets."""
    set_a = {1, 2, 3, 4, 5}
    tuple_a = (1, 2, 3, 4, 5)

    print("── Quiz 16 ──")
    print(f"  set_a = {set_a}")
    print(f"  tuple_a = {tuple_a}")
    print(f"  set_a.issubset(tuple_a) = {set_a.issubset(tuple_a)}")

    # Answer: A) True
    # issubset() accepts any iterable (list, tuple, generator, etc.)
    # It internally converts the argument to a set for comparison.
    # Since all elements of set_a are in tuple_a, it's a subset.
    #
    # Note: The <= operator requires BOTH sides to be sets:
    #   set_a <= set(tuple_a)  → True
    #   set_a <= tuple_a       → TypeError


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
