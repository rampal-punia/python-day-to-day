"""Quiz 13: round() with booleans — banker's rounding.

Difficulty: 🟡 Intermediate
Topics: round(), banker's rounding, bool as int

Question: What is the output of statement_1 == statement_2?
    A) True
    B) False
    C) Error
"""


def quiz() -> None:
    """Demonstrates 'round half to even' (banker's rounding)."""
    statement_1 = round(1.5 + True)  # round(2.5) = 2
    statement_2 = round(1.5 + False)  # round(1.5) = 2

    print("── Quiz 13 ──")
    print(f"  round(1.5 + True)  = round(2.5) = {statement_1}")
    print(f"  round(1.5 + False) = round(1.5) = {statement_2}")
    print(f"  statement_1 == statement_2: {statement_1 == statement_2}")

    # Answer: A) True
    # Explanation:
    #   1. bool is a subclass of int: True == 1, False == 0
    #   2. Python 3 uses "round half to even" (banker's rounding):
    #      round(2.5) = 2 (rounds to nearest EVEN number)
    #      round(1.5) = 2 (rounds to nearest EVEN number)
    #   3. Both equal 2, so 2 == 2 → True

    print("\n  Banker's rounding examples:")
    for val in [0.5, 1.5, 2.5, 3.5, 4.5]:
        print(f"    round({val}) = {round(val)}")


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
