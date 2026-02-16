"""Comma: Operator or Separator? — A common Python gotcha.

Difficulty: 🟡 Intermediate
Topics: comma as separator, tuple packing, operator precedence, `in`

The comma is NOT an operator in Python — it's a separator.
This means expressions separated by commas form a tuple.

    "a" in "b", "a"
    is parsed as:
    ("a" in "b"), "a"  →  (False, 'a')

    NOT as:
    "a" in ("b", "a")  →  True

Author: @rampal-punia
"""


def demo_comma_gotcha() -> None:
    """Show why comma precedence matters with `in`."""
    # Without parentheses: comma creates a tuple
    result_no_parens = "a" in "b", "a"
    print(f"  'a' in 'b', 'a'       = {result_no_parens}")  # (False, 'a')
    print(f"  Parsed as: ('a' in 'b'), 'a'")

    # With parens on the right: membership test on tuple
    result_right_parens = "a" in ("b", "a")
    print(f"\n  'a' in ('b', 'a')     = {result_right_parens}")  # True
    print(f"  Parsed as: 'a' in ('b', 'a')")

    # With parens on the left: tuple first element + separator
    result_left_parens = ("a" in "b"), "a"
    print(f"\n  ('a' in 'b'), 'a'    = {result_left_parens}")  # (False, 'a')

    # More examples of comma creating tuples
    print("\n── Comma Creates Tuples ──")
    x = 1, 2, 3
    print(f"  x = 1, 2, 3  → type: {type(x).__name__}, value: {x}")

    y = (1,)  # Single-element tuple needs trailing comma
    z = 1  # Just an integer!
    print(f"  (1,)  → type: {type(y).__name__}, value: {y}")
    print(f"  (1)   → type: {type(z).__name__}, value: {z}")


if __name__ == "__main__":
    print("── Comma: Separator, Not Operator ──\n")
    demo_comma_gotcha()

# For more on Python follow: https://x.com/rs_punia_
