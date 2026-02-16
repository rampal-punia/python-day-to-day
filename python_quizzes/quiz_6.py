"""Quiz 6: Dict keys — hash(3.0) == hash(3).

Difficulty: 🟡 Intermediate
Topics: dict keys, hash equality, float vs int, key overwriting

Question: What is the output?
    A) {1: 'Ruby', 3.0: 'Rust', 3: 'Python'}
    B) {1: 'Ruby', 3.0: 'Rust'}
    C) {1: 'Ruby', 3.0: 'Python'}
    D) Error
"""


def quiz() -> None:
    """Dict keys are compared by hash AND equality."""
    languages: dict[int | float, str] = {}
    languages[1] = "Ruby"
    languages[3.0] = "Rust"
    languages[3] = "Python"  # Overwrites 3.0 because 3 == 3.0

    print("── Quiz 6 ──")
    print(f"  languages = {languages}")
    # Answer: C) {1: 'Ruby', 3.0: 'Python'}

    # Explanation:
    print(f"\n  3.0 == 3:         {3.0 == 3}")  # True
    print(f"  hash(3.0):        {hash(3.0)}")  # 3
    print(f"  hash(3):          {hash(3)}")  # 3
    print(f"  hash(3.0)==hash(3): {hash(3.0) == hash(3)}")  # True
    print("\n  Since 3.0 == 3 and hash(3.0) == hash(3),")
    print("  Python treats them as the SAME key.")
    print("  The original key (3.0) is kept, but value is updated to 'Python'.")


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
