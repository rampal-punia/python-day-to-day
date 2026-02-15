"""
String Formatting Mastery — f-strings, format(), and % operator
================================================================
Three eras of Python string formatting, with real-world examples.

Author: @rampal-punia
"""

import math
from datetime import datetime


# ═══════════════════════════════════════════════════
# 1. F-STRINGS (Python 3.6+) — The Modern Way
# ═══════════════════════════════════════════════════

def demo_fstrings():
    name = "Alice"
    age = 28

    # Basic interpolation
    print(f"  {name} is {age} years old")

    # Expressions inside braces
    print(f"  Next year: {age + 1}")
    print(f"  Uppercase: {name.upper()}")
    print(f"  Length   : {len(name)}")

    # ── Number Formatting ──
    price = 1234567.89
    print(f"\n  Number Formatting:")
    print(f"    Commas       : {price:,.2f}")          # 1,234,567.89
    print(f"    Width 15     : {price:>15,.2f}")       # right-aligned
    print(f"    Percentage   : {0.856:.1%}")            # 85.6%
    print(f"    Scientific   : {price:.2e}")            # 1.23e+06
    print(f"    Binary       : {42:08b}")               # 00101010
    print(f"    Hex          : {255:#06x}")              # 0x00ff
    print(f"    Octal        : {8:#o}")                  # 0o10

    # ── Alignment & Padding ──
    word = "Python"
    print(f"\n  Alignment:")
    print(f"    Left   : |{word:<20}|")
    print(f"    Right  : |{word:>20}|")
    print(f"    Center : |{word:^20}|")
    print(f"    Fill * : |{word:*^20}|")

    # ── Debugging with = (Python 3.8+) ──
    x, y = 10, 20
    print(f"\n  Debug (=):")
    print(f"    {x = }")           # x = 10
    print(f"    {x + y = }")       # x + y = 30
    print(f"    {name.lower() = }")

    # ── Date Formatting ──
    now = datetime.now()
    print(f"\n  Date in f-string:")
    print(f"    {now:%Y-%m-%d %H:%M:%S}")
    print(f"    {now:%B %d, %Y}")  # February 15, 2026

    # ── Multiline f-strings ──
    item = {"name": "Laptop", "price": 999.99, "qty": 2}
    receipt = (
        f"  ┌─────────────────────────┐\n"
        f"  │ Item : {item['name']:<15} │\n"
        f"  │ Price: ${item['price']:<14.2f} │\n"
        f"  │ Qty  : {item['qty']:<15} │\n"
        f"  │ Total: ${item['price']*item['qty']:<14.2f} │\n"
        f"  └─────────────────────────┘"
    )
    print(f"\n{receipt}")


# ═══════════════════════════════════════════════════
# 2. str.format() — The Classic Way
# ═══════════════════════════════════════════════════

def demo_str_format():
    # Positional arguments
    print("  {} and {}".format("Alice", "Bob"))

    # Numbered arguments (reusable)
    print("  {0} vs {1}, {0} wins!".format("Python", "Java"))

    # Named arguments
    print("  {name} scored {score}%".format(name="Alice", score=95))

    # Accessing dict/list items
    person = {"name": "Bob", "age": 30}
    print("  {p[name]} is {p[age]}".format(p=person))

    # Format spec
    pi = math.pi
    print(f"\n  Format spec with .format():")
    print("  Pi = {:.4f}".format(pi))
    print("  Pi = {:>10.2f}".format(pi))


# ═══════════════════════════════════════════════════
# 3. % OPERATOR — The Legacy Way (C-style)
# ═══════════════════════════════════════════════════

def demo_percent_formatting():
    """Still seen in logging and legacy codebases."""
    name = "Charlie"
    age = 25
    gpa = 3.87

    print("  %s is %d years old" % (name, age))
    print("  GPA: %.2f" % gpa)
    print("  Hex: %x, Oct: %o" % (255, 8))
    print("  Padded: %10s | %-10s" % ("right", "left"))


# ═══════════════════════════════════════════════════
# 4. TEMPLATE STRINGS — Safe User Input
# ═══════════════════════════════════════════════════

def demo_template_strings():
    """Template strings are safe from injection attacks."""
    from string import Template

    t = Template("Hello, $name! You have $$${amount} in your account.")
    result = t.substitute(name="Alice", amount=500)
    print(f"  {result}")

    # safe_substitute doesn't raise on missing keys
    t2 = Template("$greeting, $name!")
    result2 = t2.safe_substitute(greeting="Hi")  # $name stays as-is
    print(f"  Safe: {result2}")


# ═══════════════════════════════════════════════════
# 5. COMPARISON TABLE
# ═══════════════════════════════════════════════════
#
# ┌─────────────┬──────────────┬───────────────┬──────────────┐
# │ Feature     │ f-strings    │ .format()     │ % operator   │
# ├─────────────┼──────────────┼───────────────┼──────────────┤
# │ Speed       │ Fastest ⚡   │ Medium        │ Slow         │
# │ Readability │ Best ✅      │ Good          │ Poor         │
# │ Expressions │ Yes          │ Limited       │ No           │
# │ Python ver  │ 3.6+         │ 2.6+          │ All          │
# │ Use case    │ Default      │ Templates     │ Logging      │
# └─────────────┴──────────────┴───────────────┴──────────────┘


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. F-Strings (Modern Python)", demo_fstrings),
        ("2. str.format() (Classic)", demo_str_format),
        ("3. % Operator (Legacy)", demo_percent_formatting),
        ("4. Template Strings (Safe)", demo_template_strings),
    ]
    for title, fn in sections:
        print("=" * 55)
        print(title)
        print("=" * 55)
        fn()
        print()
