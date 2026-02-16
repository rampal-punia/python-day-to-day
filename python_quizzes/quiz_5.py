"""Quiz 5: Shadowing built-in names (max).

Difficulty: 🟡 Intermediate
Topics: name shadowing, builtins module, built-in functions

Question: What happens when you assign max = 100 then call max(numbers)?
    A) 0
    B) TypeError
    C) SyntaxError
    D) 1
"""

import builtins


def quiz() -> None:
    """Assigning to 'max' shadows the built-in max() function."""
    print("── Quiz 5 ──")

    max = 100  # noqa: A001 — shadows built-in!  # type: ignore
    numbers = list(range(10))

    try:
        print(f"  max(numbers) = ", end="")
        result = max(numbers)  # type: ignore[operator]
        print(result)
    except TypeError as e:
        print(f"TypeError: {e}")

    # Answer: B) TypeError
    # 'max' is now the integer 100, not the built-in function.
    # Calling 100([0,1,...,9]) raises TypeError.

    # Workaround: use builtins module
    real_max = builtins.max(numbers)
    print(f"  builtins.max(numbers) = {real_max}")
    print("\n  Lesson: Never shadow built-in names like max, min, list, etc.")


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
