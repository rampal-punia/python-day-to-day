"""capitalize() vs title() — Two similar but different case methods.

Difficulty: 🟢 Easy
Topics: str.capitalize(), str.title(), str.upper(), str.lower(), str.swapcase()

capitalize() → First letter of the STRING is uppercased, rest lowered.
title()      → First letter of EACH WORD is uppercased, rest lowered.

Author: @rampal-punia
"""


def case_methods_demo() -> None:
    """Compare all case-related string methods."""
    text = "learning PYTHON is Fun"

    print(f"  Original:    '{text}'")
    print(f"  capitalize():'{text.capitalize()}'")
    print(f"  title():     '{text.title()}'")
    print(f"  upper():     '{text.upper()}'")
    print(f"  lower():     '{text.lower()}'")
    print(f"  swapcase():  '{text.swapcase()}'")
    print(f"  casefold():  '{text.casefold()}'")


def title_vs_capitalize_edge_cases() -> None:
    """Show edge cases where title() and capitalize() behave differently."""
    print("\n── Edge Cases ──")

    # title() capitalizes after ANY non-alpha character
    s = "it's a test-case"
    print(f"  '{s}'.title()      → '{s.title()}'")
    # 'It'S A Test-Case' — note the 'S' after apostrophe!

    # capitalize() only affects the very first character
    print(f"  '{s}'.capitalize() → '{s.capitalize()}'")

    # Already uppercase letters are lowered by both
    s2 = "HELLO WORLD"
    print(f"  '{s2}'.capitalize() → '{s2.capitalize()}'")
    print(f"  '{s2}'.title()      → '{s2.title()}'")


if __name__ == "__main__":
    print("── Case Methods Comparison ──\n")
    case_methods_demo()
    title_vs_capitalize_edge_cases()

# For more on Python follow: https://x.com/rs_punia_
