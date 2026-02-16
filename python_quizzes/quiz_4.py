"""Quiz 4: callable() — What is callable in Python?

Difficulty: 🟡 Intermediate
Topics: callable(), type objects, instances, int(), str()

Question: What does callable() return for [int, '', 1, str]?

Key insight:
    int, str  → callable (they are TYPE objects / constructors)
    int(), str() → NOT callable (they are INSTANCES: 0 and '')
    '', 1     → NOT callable (instances of str and int)
"""


def quiz() -> None:
    """callable() checks if an object can be called like a function."""
    print("── Quiz 4 ──")

    # Types are callable (they are constructors)
    elements = [int, "", 1, str]
    result = [callable(obj) for obj in elements]
    print(f"  [int, '', 1, str]     → {result}")  # [True, False, False, True]

    # Instances are NOT callable
    elements2 = [int(), "", 1, str()]
    result2 = [callable(obj) for obj in elements2]
    print(f"  [int(), '', 1, str()] → {result2}")  # [False, False, False, False]

    # Note: int() returns 0, str() returns '' — both are instances
    print(f"\n  int() = {int()!r}, str() = {str()!r}")
    print(f"  callable(int) = {callable(int)}, callable(0) = {callable(0)}")


if __name__ == "__main__":
    quiz()
