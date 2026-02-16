"""Random Hex Colors — 5 methods to generate hex color codes.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: random, secrets, hex formatting, f-strings

Format: #RRGGBB where each pair is a 2-digit hex value (00-FF)

Author: @rampal-punia
"""

import random
import secrets


# 🟢 Method 1: Three separate randint calls
def hex_color_v1() -> str:
    """Generate hex color from three randint(0, 255) calls."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02X}{g:02X}{b:02X}"


# 🟢 Method 2: Single randint for full range
def hex_color_v2() -> str:
    """Generate hex color from a single random integer."""
    return f"#{random.randint(0, 0xFFFFFF):06X}"


# 🟡 Method 3: secrets module (cryptographically secure)
def hex_color_v3() -> str:
    """Generate hex color using secrets.token_hex (secure random)."""
    return f"#{secrets.token_hex(3).upper()}"


# 🟢 Method 4: random.choices from hex digits
def hex_color_v4() -> str:
    """Generate hex color by picking 6 random hex digits."""
    return "#" + "".join(random.choices("0123456789ABCDEF", k=6))


# 🟢 Method 5: format() with randrange
def hex_color_v5() -> str:
    """Generate hex color using format() and randrange."""
    return "#{:06X}".format(random.randrange(16**6))


if __name__ == "__main__":
    methods = [
        ("randint (3x)", hex_color_v1),
        ("randint (1x)", hex_color_v2),
        ("secrets", hex_color_v3),
        ("random.choices", hex_color_v4),
        ("format+randrange", hex_color_v5),
    ]

    print("── Random Hex Colors ──")
    for name, func in methods:
        print(f"  {name:<18}: {func()}")

# For more on Python follow: https://x.com/rs_punia_
