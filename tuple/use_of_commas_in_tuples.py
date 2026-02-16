"""Commas in Tuples — It's the comma, not the parentheses!

Difficulty: 🟢 Easy
Topics: tuple packing, trailing comma, type(), parentheses vs commas

Key insight: The COMMA creates a tuple, not the parentheses.
    t = 1, 2, 3     → tuple
    t = (1, 2, 3)   → tuple  (parentheses are optional)
    t = 1,           → tuple  (single-element, trailing comma!)
    t = (1)          → int    (just grouping, no comma)
    t = (1,)         → tuple  (trailing comma makes it a tuple)

Author: @rampal-punia
"""


def demo_comma_tuples() -> None:
    """Show that commas, not parentheses, create tuples."""
    examples: list[tuple[str, object]] = [
        ("(1, 2, 3)", (1, 2, 3)),
        ("1, 2, 3", (1, 2, 3)),  # Same as above!
        ("1,", (1,)),  # Single-element tuple
        ("(1,)", (1,)),  # Same as above
        ("(1)", (1)),  # NOT a tuple — just int!
    ]

    print("── Commas Create Tuples ──")
    for expr, value in examples:
        print(f"  {expr:<12} → type: {type(value).__name__:<6} value: {value}")

    # Common gotcha: function call with single argument
    print("\n── Common Gotcha: Function Arguments ──")
    print(f"  len((1, 2, 3))  = {len((1, 2, 3))}")  # 3 (tuple arg)
    # print(f"  len(1, 2, 3)")  # TypeError! 3 separate args
    print("  len(1, 2, 3)    = TypeError (3 separate args, not a tuple)")


if __name__ == "__main__":
    demo_comma_tuples()

# For more on Python follow: https://x.com/rs_punia_
