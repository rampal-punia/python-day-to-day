"""None Demo — Understanding Python's None and multiplication quirks.

Difficulty: 🟢 Easy
Topics: None, NoneType, multiplication operator, type errors

Python's * operator works differently depending on the type:
    int * int   → arithmetic multiplication (5 * 2 = 10)
    int * str   → string repetition       (3 * 'ab' = 'ababab')
    int * list  → list repetition          (2 * [1] = [1, 1])
    int * bool  → arithmetic (bool is int) (5 * True = 5)
    int * None  → TypeError!

Author: @rampal-punia
"""


def multiplication_demo() -> None:
    """Show how * behaves with different types."""
    examples: list[tuple[str, object]] = [
        ("5 * True", 5 * True),  # 5 (True == 1)
        ("5 * False", 5 * False),  # 0 (False == 0)
        ('5 * "Spam"', 5 * "Spam"),  # SpamSpamSpamSpamSpam
        ("5 * [1, 2]", 5 * [1, 2]),  # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    ]

    print("── Multiplication With Different Types ──")
    for expr, result in examples:
        print(f"  {expr:<15} = {result}")

    # None causes a TypeError
    print("\n── Multiplying with None ──")
    try:
        result = 5 * None  # type: ignore[operator]
    except TypeError as e:
        print(f"  5 * None → TypeError: {e}")

    print(f"\n  type(None) = {type(None)}")
    print(f"  None is None: {None is None}")
    print(f"  bool(None):   {bool(None)}  (falsy)")


if __name__ == "__main__":
    multiplication_demo()
