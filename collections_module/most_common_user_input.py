"""Most Common Letters (User Input) — Analyze any text from the user.

Difficulty: 🟢 Easy
Topics: collections.Counter, input(), string cleaning, character frequency

Author: @rampal-punia
"""

import re
from collections import Counter


def clean_text(text: str) -> str:
    """Remove all non-alphabetic characters from text.

    Uses regex instead of chaining multiple .replace() calls,
    which would miss characters like !, ?, ;, :, etc.

    Args:
        text: Raw input string.

    Returns:
        Cleaned lowercase string with only letters.
    """
    return re.sub(r"[^a-zA-Z]", "", text).lower()


def analyze_user_input() -> None:
    """Get text from user, count letter frequencies, and display results."""
    raw_text = input("Enter a string: ")
    cleaned = clean_text(raw_text)

    if not cleaned:
        print("  No letters found in the input.")
        return

    counts = Counter(cleaned)

    print("\n── Letter Frequencies ──")
    for letter, count in sorted(counts.items()):
        bar = "█" * count
        print(f"  {letter}: {count:>3} {bar}")

    print(f"\n  Top 3 most common: {counts.most_common(3)}")
    print(f"  Total letters:     {sum(counts.values())}")
    print(f"  Unique letters:    {len(counts)}")


if __name__ == "__main__":
    analyze_user_input()

# For more on Python follow: https://x.com/rs_punia_
