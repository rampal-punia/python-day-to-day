"""Quiz 9: set.difference() vs `-` operator.

Difficulty: 🟡 Intermediate
Topics: set.difference(), minus operator, type requirements

Question: Which method works?
    A) Only Method A will work
    B) Only Method B will work
    C) Both methods (A & B) will work
    D) Both methods will generate an Error
"""


def quiz() -> None:
    """difference() accepts any iterable, but - requires a set."""
    my_set = {1, 2, 3}
    my_list = [3, 4, 5]

    print("── Quiz 9 ──")

    # Method A: .difference() accepts any iterable
    result_a = my_set.difference(my_list)
    print(f"  Method A: set.difference(list) = {result_a}")  # {1, 2}

    # Method B: - operator requires BOTH operands to be sets
    try:
        result_b = my_set - my_list  # type: ignore[operator]
        print(f"  Method B: set - list = {result_b}")
    except TypeError as e:
        print(f"  Method B: set - list = TypeError: {e}")

    # Answer: A) Only Method A will work
    # .difference() accepts any iterable (list, tuple, etc.)
    # The - operator requires both sides to be sets.
    print("\n  .difference() takes any iterable")
    print("  The - operator requires both operands to be sets")
    print(f"  set - set works: {my_set - {3, 4, 5}}")


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
