"""Quiz: Comma Creates a Tuple — type() and representation.

Difficulty: 🟢 Easy
Topics: trailing comma, tuple packing, __str__, __repr__
"""


def quiz() -> None:
    """What does `t = 1,` create?"""
    t = (1,)

    print("── Quiz: Comma Tuple ──")
    print(f"  t = 1,")
    print(f"  type(t)      = {type(t)}")  # <class 'tuple'>
    print(f"  t.__str__()  = {t.__str__()}")  # (1,)
    print(f"  t.__repr__() = {t.__repr__()}")  # (1,)

    # Explanation: The trailing comma after `1` packs it into a
    # single-element tuple. Parentheses are optional.


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
