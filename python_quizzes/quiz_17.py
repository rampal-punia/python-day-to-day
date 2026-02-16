"""Quiz 17: Walrus operator (:=) precedence.

Difficulty: 🔴 Advanced
Topics: walrus operator, operator precedence, := vs in

Question: What is the output?
    A) 4
    B) 2
    C) NameError: name 'n' is not defined
    D) 3
"""


def quiz() -> None:
    """`:=` has LOWER precedence than `in`."""
    nums = [1, 2, 3, 4, 5]

    # This is parsed as:  n := (3 in nums)  →  n := True
    # NOT as:             (n := 3) in nums  →  3 in nums
    if n := 3 in nums:
        result = n + 1

    print("── Quiz 17 ──")
    print(f"  n := 3 in nums")
    print(f"  n = {n!r}")  # True (bool)
    print(f"  n + 1 = {result}")  # True + 1 = 2

    # Answer: B) 2
    # Step by step:
    #   1. `3 in nums` evaluates first → True
    #   2. `n := True` assigns True to n
    #   3. `if True:` enters the branch
    #   4. `True + 1` = 2  (bool is subclass of int)
    #
    # To get the expected behavior (n=3, then check membership):
    #   if (n := 3) in nums:  → n=3, prints 4


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
