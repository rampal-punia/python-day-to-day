"""Value from Base — Convert digit strings to integers with any base.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: positional notation, base conversion, int(value, base)

How positional notation works:
    '20' in base 10 = 2×10¹ + 0×10⁰ = 20
    '20' in base  2 = 2×2¹  + 0×2⁰  = 4 (invalid: '2' not in base 2!)
    '20' in base  8 = 2×8¹  + 0×8⁰  = 16
    '20' in base 16 = 2×16¹ + 0×16⁰ = 32

Author: @rampal-punia
"""


# 🟢 Method 1: Manual positional calculation (educational)
def value_from_base_manual(digits: str, base: int = 10) -> int:
    """Convert a digit string to an integer using positional notation.

    Supports digits 0-9 and a-f (for bases > 10).

    Args:
        digits: String of digits (e.g., '1a', '20', 'ff').
        base: The number base (2-36).

    Returns:
        The integer value.

    Raises:
        ValueError: If a digit is invalid for the given base.
    """
    result = 0
    for ch in digits.lower():
        if ch.isdigit():
            d = int(ch)
        elif ch.isalpha():
            d = ord(ch) - ord("a") + 10
        else:
            raise ValueError(f"Invalid character: {ch!r}")
        if d >= base:
            raise ValueError(f"Digit '{ch}' invalid for base {base}")
        result = result * base + d
    return result


# 🟢 Method 2: Built-in int() (recommended)
def value_from_base_builtin(digits: str, base: int = 10) -> int:
    """Convert a digit string to an integer using Python's built-in int()."""
    return int(digits, base)


if __name__ == "__main__":
    print("── Manual Positional Calculation ──")
    for val, base in [("20", 10), ("20", 8), ("20", 16), ("ff", 16), ("101", 2)]:
        result = value_from_base_manual(val, base)
        print(f"  '{val}' base {base:>2} = {result}")

    print("\n── Built-in int(value, base) ──")
    for val, base in [("20", 10), ("20", 8), ("0xff", 16), ("0b1010", 2)]:
        result = int(val, base)
        print(f"  int('{val}', {base}) = {result}")

    print("\n── Verification ──")
    assert value_from_base_manual("ff", 16) == int("ff", 16) == 255
    assert value_from_base_manual("101", 2) == int("101", 2) == 5
    print("  ✅ Manual and built-in methods agree.")
