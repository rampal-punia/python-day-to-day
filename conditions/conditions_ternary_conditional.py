"""Ternary Conditional Expressions — Inline if/else in Python.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: ternary operator, chained ternary, conditional expression

Syntax:  value_if_true  if  condition  else  value_if_false

Chained ternaries evaluate LEFT to RIGHT:
    "Hello" if a else "Bye" if b else "Hi"
    is parsed as:
    "Hello" if a else ("Bye" if b else "Hi")

Author: @rampal-punia
"""


def ternary_basics() -> None:
    """Demonstrate basic and chained ternary expressions."""
    # 🟢 Easy: Basic ternary
    age = 20
    status = "adult" if age >= 18 else "minor"
    print(f"  age={age} → {status}")

    # 🟢 Easy: Ternary with bool values
    a = bool(0)  # False
    b = bool(1)  # True
    print(f"  a=bool(0)={a}, b=bool(1)={b}")

    # 🟡 Intermediate: Chained ternary (tricky!)
    # Parsed as: "Hello" if False else ("Bye" if True else "Hi")
    result = "Hello" if a else "Bye" if b else "Hi"
    print(f"  'Hello' if a else 'Bye' if b else 'Hi' → '{result}'")

    # Step-by-step:
    # 1. a is False, so skip "Hello"
    # 2. Evaluate: "Bye" if b else "Hi"
    # 3. b is True, so result = "Bye"


def ternary_patterns() -> None:
    """Show common ternary patterns in Python."""
    # Assigning defaults
    user_input: str | None = None
    name = user_input if user_input else "Anonymous"
    print(f"\n  Default: {name}")

    # Inline min/max
    x, y = 10, 20
    smaller = x if x < y else y
    print(f"  Min({x}, {y}) = {smaller}")

    # Ternary in f-string
    count = 1
    print(f"  {count} item{'s' if count != 1 else ''}")
    count = 5
    print(f"  {count} item{'s' if count != 1 else ''}")

    # Ternary in list comprehension
    numbers = [1, 2, 3, 4, 5, 6]
    labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
    print(f"  Labels: {labels}")


if __name__ == "__main__":
    print("── Ternary Basics ──")
    ternary_basics()

    print("\n── Ternary Patterns ──")
    ternary_patterns()
