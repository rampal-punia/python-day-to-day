"""Bool Arithmetic — Why True == 1 and False == 0 in Python.

Difficulty: 🟢 Easy
Topics: bool subclass of int, PEP 285, isinstance, lambda

bool is a subclass of int (PEP 285), so:
    True  == 1  and  False == 0
    True + True == 2
    5 * True == 5
    (5 * 4) - True == 19

Author: @rampal-punia
"""


def demonstrate_bool_as_int() -> None:
    """Show that bool is a subclass of int with examples."""
    print("── Bool is a Subclass of Int ──")
    print(f"  issubclass(bool, int): {issubclass(bool, int)}")
    print(f"  isinstance(True, int): {isinstance(True, int)}")
    print(f"  True == 1:  {True == 1}")
    print(f"  False == 0: {False == 0}")

    print("\n── Bool in Arithmetic ──")
    print(f"  True + True    = {True + True}")  # 2
    print(f"  True + False   = {True + False}")  # 1
    print(f"  5 * True       = {5 * True}")  # 5
    print(f"  5 * False      = {5 * False}")  # 0
    print(f"  sum([True, False, True]) = {sum([True, False, True])}")  # 2

    # The original puzzle
    print("\n── The Puzzle ──")
    result = (lambda a, b: a * b)(5, 4) - True
    print(f"  (lambda a, b: a * b)(5, 4) - True")
    print(f"  = (5 * 4) - 1")
    print(f"  = 20 - 1")
    print(f"  = {result}")


if __name__ == "__main__":
    demonstrate_bool_as_int()

# For more on Python follow: https://x.com/rs_punia_
