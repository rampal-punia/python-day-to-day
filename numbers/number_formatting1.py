"""Number Formatting in Python — f-string format specifiers.

Difficulty: 🟢 Easy
Topics: f-strings, format specifiers, thousands separator, percentage

Format mini-language reference:
    :,       → Thousands separator (commas)
    :.2f     → 2 decimal places (fixed-point)
    :.2%     → Percentage with 2 decimal places
    :g       → General format (strip trailing zeros)
    :>10     → Right-align in 10 chars
    :0>5     → Zero-pad to 5 chars
    :_       → Underscore as thousands separator

Author: @rampal-punia
"""


def format_population_stats() -> None:
    """Demonstrate number formatting with real-world data."""
    population = 80_000_000
    in_city = 55_222_222
    in_village = population - in_city
    city_pct = in_city / population
    village_pct = in_village / population

    print("── Population Statistics ──")
    print(f"  Total:        {population:>15,}")  # 80,000,000
    print(f"  In city:      {in_city:>15,}")  # 55,222,222
    print(f"  In village:   {in_village:>15,.2f}")  # 24,777,778.00
    print(f"  City %:       {city_pct:>15.4f}")  # 0.6903
    print(f"  Village %:    {village_pct:>14.2%}")  # 30.97%
    print(f"  General fmt:  {population:g}")  # strips .00


def format_specifier_cheatsheet() -> None:
    """Show common f-string format specifiers."""
    n = 42
    pi = 3.14159265
    big = 1_234_567_890

    print("\n── Format Specifier Cheatsheet ──")
    print(f"  Decimal places:  {pi:.2f}")  # 3.14
    print(f"  Scientific:      {big:.2e}")  # 1.23e+09
    print(f"  Percentage:      {0.8567:.1%}")  # 85.7%
    print(f"  Thousands (,):   {big:,}")  # 1,234,567,890
    print(f"  Thousands (_):   {big:_}")  # 1_234_567_890
    print(f"  Zero-pad:        {n:05d}")  # 00042
    print(f"  Right-align:     '{n:>10d}'")  # '        42'
    print(f"  Left-align:      '{n:<10d}'")  # '42        '
    print(f"  Center:          '{n:^10d}'")  # '    42    '
    print(f"  Binary:          {n:b}")  # 101010
    print(f"  Hex:             {n:#x}")  # 0x2a
    print(f"  Octal:           {n:#o}")  # 0o52


if __name__ == "__main__":
    format_population_stats()
    format_specifier_cheatsheet()

# For more on Python follow: https://x.com/rs_punia_
