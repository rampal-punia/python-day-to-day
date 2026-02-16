"""Datetime Format Codes — strftime() and strptime() reference.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: strftime, strptime, format codes, date formatting, parsing

strftime() = format a datetime object INTO a string
strptime() = PARSE a string into a datetime object

Author: @rampal-punia
"""

import datetime

# ────────────────────────────────────────────────────────────────
# FORMAT CODE REFERENCE
# ────────────────────────────────────────────────────────────────
FORMAT_CODES: dict[str, str] = {
    "%a": "Weekday abbreviated (Mon)",
    "%A": "Weekday full name (Monday)",
    "%w": "Weekday number (0=Sunday, 6=Saturday)",
    "%d": "Day of month zero-padded (01-31)",
    "%b": "Month abbreviated (Jan)",
    "%B": "Month full name (January)",
    "%m": "Month zero-padded (01-12)",
    "%y": "Year without century (25)",
    "%Y": "Year with century (2025)",
    "%H": "Hour 24-hour zero-padded (00-23)",
    "%I": "Hour 12-hour zero-padded (01-12)",
    "%p": "AM or PM",
    "%M": "Minute zero-padded (00-59)",
    "%S": "Second zero-padded (00-59)",
    "%f": "Microsecond zero-padded (000000-999999)",
    "%z": "UTC offset (±HHMM)",
    "%Z": "Time zone name",
    "%j": "Day of year zero-padded (001-366)",
    "%U": "Week number (Sunday start, 00-53)",
    "%W": "Week number (Monday start, 00-53)",
    "%c": "Locale date and time",
    "%x": "Locale date",
    "%X": "Locale time",
}


def demo_format_codes() -> None:
    """Demonstrate all strftime format codes with live output."""
    now = datetime.datetime.now()
    print(f"  Current datetime: {now}\n")

    print(f"  {'Code':<6} {'Description':<42} {'Output'}")
    print(f"  {'----':<6} {'-' * 42} {'------'}")
    for code, desc in FORMAT_CODES.items():
        try:
            output = now.strftime(code)
            print(f"  {code:<6} {desc:<42} {output}")
        except ValueError:
            print(f"  {code:<6} {desc:<42} (not available)")


def demo_common_patterns() -> None:
    """Show commonly used date/time formatting patterns."""
    day = datetime.datetime(2021, 11, 20, 14, 30, 45)

    patterns = [
        ("%Y-%m-%d", "ISO date"),
        ("%d/%m/%Y", "European date"),
        ("%m/%d/%Y", "US date"),
        ("%B %d, %Y", "Long date"),
        ("%A, %B %d, %Y", "Full date with weekday"),
        ("%H:%M:%S", "24-hour time"),
        ("%I:%M %p", "12-hour time"),
        ("%Y-%m-%d %H:%M:%S", "Datetime stamp"),
    ]

    print(f"\n  Formatting: {day}")
    print(f"  {'Pattern':<26} {'Name':<24} {'Output'}")
    print(f"  {'-' * 26} {'-' * 24} {'------'}")
    for pattern, name in patterns:
        print(f"  {pattern:<26} {name:<24} {day.strftime(pattern)}")

    # Also show strptime (parsing)
    print("\n  Parsing with strptime():")
    date_str = "20-Nov-2021 14:30"
    parsed = datetime.datetime.strptime(date_str, "%d-%b-%Y %H:%M")
    print(f"  '{date_str}' → {parsed}")


if __name__ == "__main__":
    print("── Format Code Reference ──")
    demo_format_codes()

    print("\n── Common Formatting Patterns ──")
    demo_common_patterns()
