"""String Concatenation — Different ways to combine strings in Python.

Difficulty: 🟢 Easy
Topics: + operator, join(), f-strings, string multiplication

The + operator concatenates strings (does NOT add numbers when used with strings).

Author: @rampal-punia
"""


def concatenation_demo() -> None:
    """Demonstrate string concatenation with the + operator."""
    print("── String Concatenation with + ──")

    x = "5"
    y = "2"
    # + between strings concatenates, doesn't add
    print(f"  '5' + '2' = '{x + y}'  (not 7!)")
    print(f"   5  +  2  = {5 + 2}    (integer addition)")


def join_demo() -> None:
    """Demonstrate join() — the efficient way to combine many strings."""
    print("\n── join() for combining sequences ──")

    words = ["Python", "is", "awesome"]
    print(f"  ' '.join({words}) = '{' '.join(words)}'")
    print(f"  '-'.join({words}) = '{'-'.join(words)}'")
    print(f"  ''.join({words})  = '{''.join(words)}'")


def multiplication_demo() -> None:
    """Demonstrate string repetition with *."""
    print("\n── String Repetition with * ──")

    print(f"  'Ha' * 3 = '{'Ha' * 3}'")
    print(f"  '-' * 20 = '{'-' * 20}'")


if __name__ == "__main__":
    concatenation_demo()
    join_demo()
    multiplication_demo()

# For more on Python follow: https://x.com/rs_punia_
