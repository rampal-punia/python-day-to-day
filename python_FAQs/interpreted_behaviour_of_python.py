"""Name Binding & Function Reassignment in Python.

Difficulty: 🟡 Intermediate
Topics: name binding, first-class functions, variable references

Key insight: In Python, functions are objects. When you assign
a function to a variable, you're copying the REFERENCE.
Redefining the function name later does NOT affect the old reference.

Author: @rampal-punia
"""


def demo_name_binding() -> None:
    """Show how function name reassignment works."""

    def func(x: int) -> int:
        return x * 3

    # new_func now points to the SAME function object as func
    new_func = func

    # Redefining 'func' creates a NEW function object
    # new_func still points to the original (x * 3)
    def func(x: int) -> int:  # noqa: F811
        return x + 2

    my_func = func  # Points to the NEW function (x + 2)

    print("── Name Binding Demo ──")
    print(f"  new_func(2) = {new_func(2)}")  # 6  (original: 2 * 3)
    print(f"  my_func(2)  = {my_func(2)}")  # 4  (redefined: 2 + 2)
    print(f"  func(2)     = {func(2)}")  # 4  (same as my_func)

    # Proof: new_func and func are different objects
    print(f"\n  new_func is func: {new_func is func}")  # False
    print(f"  my_func is func:  {my_func is func}")  # True


if __name__ == "__main__":
    demo_name_binding()
