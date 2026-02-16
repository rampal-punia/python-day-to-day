"""Tuple __repr__ — Understanding object representation.

Difficulty: 🟢 Easy
Topics: __repr__, __str__, tuple packing, type(), mixed containers

When you write `a = [1, 2], (1, 2)`, the comma creates a TUPLE
containing a list and a tuple. This is called 'tuple packing'.

    a.__repr__()  → '([1, 2], (1, 2))'   (unambiguous representation)
    a.__str__()   → '([1, 2], (1, 2))'   (human-readable, same here)

Author: @rampal-punia
"""


def demo_tuple_repr() -> None:
    """Show __repr__ vs __str__ for tuples."""
    # Comma creates a tuple (no parentheses needed)
    a = [1, 2], (1, 2)

    print("── Tuple Representation ──")
    print(f"  a              = {a}")
    print(f"  type(a)        = {type(a)}")
    print(f"  a.__repr__()   = {a.__repr__()}")
    print(f"  a.__str__()    = {a.__str__()}")
    print(f"  repr(a)        = {repr(a)}")

    # What's inside?
    print(f"\n  a[0] = {a[0]}  (type: {type(a[0]).__name__})")
    print(f"  a[1] = {a[1]}  (type: {type(a[1]).__name__})")

    # repr vs str difference (visible with strings)
    print("\n── repr vs str (visible difference with strings) ──")
    s = "hello\nworld"
    print(f"  str(s):  {str(s)}")
    print(f"  repr(s): {repr(s)}")


if __name__ == "__main__":
    demo_tuple_repr()
