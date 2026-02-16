"""Quiz 1: int() with a base argument.

Difficulty: 🟡 Intermediate
Topics: int(), base conversion, octal

Question: What is the output of int("40", base=8)?
    A: 40
    B: 32
    C: 8
    D: Error
"""


def quiz() -> None:
    """int('40', base=8) treats '40' as octal."""
    x = "40"
    result = int(x, base=8)

    print("── Quiz 1 ──")
    print(f"  int('40', base=8) = {result}")
    # Answer: B (32)
    # Explanation: In octal, '40' = 4×8¹ + 0×8⁰ = 32


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
