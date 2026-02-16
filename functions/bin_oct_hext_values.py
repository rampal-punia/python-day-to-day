"""Binary, Octal, and Hexadecimal — Number base conversions in Python.

Difficulty: 🟢 Easy
Topics: bin(), oct(), hex(), f-string formatting, int() with base

Python provides built-in functions AND format specifiers for
converting integers to/from different number bases.

Author: @rampal-punia
"""


def show_base_conversions(number: int) -> None:
    """Display a number in binary, octal, and hexadecimal.

    Args:
        number: The integer to convert.
    """
    print(f"  Decimal:     {number}")

    # Method 1: Built-in functions (include prefix 0b, 0o, 0x)
    print(f"  bin()   →    {bin(number)}")
    print(f"  oct()   →    {oct(number)}")
    print(f"  hex()   →    {hex(number)}")

    # Method 2: f-string format specifiers (no prefix, cleaner)
    print(f"  f'{{:b}}' →    {number:b}")
    print(f"  f'{{:o}}' →    {number:o}")
    print(f"  f'{{:x}}' →    {number:x}")
    print(f"  f'{{:X}}' →    {number:X}")  # Uppercase hex

    # Method 3: With zero-padding
    print(f"  f'{{:08b}}' →  {number:08b}")  # 8-bit binary
    print(f"  f'{{:04x}}' →  {number:04x}")  # 4-digit hex


def convert_from_base(value: str, base: int) -> int:
    """Convert a string representation in a given base to decimal.

    Args:
        value: String like '0b1010', '0o17', '0xFF', or plain '42'.
        base: The base (2, 8, 10, 16, etc.).

    Returns:
        The decimal integer value.
    """
    return int(value, base)


if __name__ == "__main__":
    print("── Base Conversions for 72 ──")
    show_base_conversions(72)

    print("\n── Base Conversions for 255 ──")
    show_base_conversions(255)

    print("\n── Convert FROM other bases to decimal ──")
    examples = [
        ("1010", 2),  # Binary 1010 = 10
        ("17", 8),  # Octal 17 = 15
        ("FF", 16),  # Hex FF = 255
        ("0b11111111", 0),  # Auto-detect prefix (base=0)
    ]
    for val, base in examples:
        result = convert_from_base(val, base)
        print(f"  int('{val}', {base}) = {result}")
