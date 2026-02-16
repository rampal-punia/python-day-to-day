"""Parameters vs Arguments — Know the difference.

Difficulty: 🟢 Easy
Topics: parameters, arguments, function definition vs call

Parameters = variables in the function DEFINITION (placeholders)
Arguments  = actual values passed in the function CALL

Mnemonic:
    Parameters → Placeholders (P ↔ P)
    Arguments  → Actual values (A ↔ A)

Author: @rampal-punia
"""


def area(length: float, width: float) -> float:
    """Calculate the area of a rectangle.

    'length' and 'width' are PARAMETERS (placeholders).

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area (length * width).
    """
    return length * width


def greet(name: str, greeting: str = "Hello") -> str:
    """Greet someone. 'greeting' has a default value.

    Args:
        name: The person's name (positional argument).
        greeting: The greeting word (keyword argument with default).
    """
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    # 10, 20 are ARGUMENTS (actual values)
    result = area(10, 20)
    print("── Parameters vs Arguments ──")
    print(f"  area(10, 20) = {result}")
    print(f"  Positional args:  area(10, 20)")
    print(f"  Keyword args:     area(length=10, width=20)")
    print(f"  Mixed:            area(10, width=20)")

    print("\n── Default Parameters ──")
    print(f"  greet('Alice')            = {greet('Alice')}")
    print(f"  greet('Alice', 'Hey')     = {greet('Alice', 'Hey')}")
    print(f"  greet(name='Bob')         = {greet(name='Bob')}")

# For more on Python follow: https://x.com/rs_punia_
