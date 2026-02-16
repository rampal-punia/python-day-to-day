"""Operator Polymorphism — The + operator behaves differently per type.

Difficulty: 🟢 Easy
Topics: operator overloading, polymorphism, __add__, TypeError

Python's + operator dispatches to the __add__ method of the left operand.
Different types implement __add__ differently:
    int + int     → arithmetic addition
    str + str     → concatenation
    list + list   → list concatenation
    tuple + tuple → tuple concatenation
    set + set     → TypeError! (use | for union)

Author: @rampal-punia
"""


def demo_operator_polymorphism() -> None:
    """Demonstrate how + behaves differently for each type."""
    examples: list[tuple[str, str, object]] = [
        ("int", "1 + 2", 1 + 2),
        ("float", "1.5 + 2.5", 1.5 + 2.5),
        ("str", "'Hello' + ' world'", "Hello" + " world"),
        ("str", "'5' + '2'", "5" + "2"),  # '52' not 7!
        ("list", "[1,2,3] + [4,5,6]", [1, 2, 3] + [4, 5, 6]),
        ("tuple", "(1,2,3) + (4,5,6)", (1, 2, 3) + (4, 5, 6)),
    ]

    print("── Operator Polymorphism: + ──\n")
    for type_name, expr, result in examples:
        print(f"  {type_name:<6} {expr:<25} = {result}")

    # set + set raises TypeError
    print(f"\n  {'set':<6} {{1,2,3}} + {{2,3,4}}", end="")
    try:
        {1, 2, 3} + {2, 3, 4}  # type: ignore[operator]
    except TypeError as e:
        print(f"         = TypeError: {e}")

    # Use | for set union instead
    print(f"  {'set':<6} {{1,2,3}} | {{2,3,4}}          = {({1, 2, 3} | {2, 3, 4})}")


if __name__ == "__main__":
    demo_operator_polymorphism()
