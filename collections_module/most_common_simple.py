"""Most Common Letters — Find the most frequent characters using Counter.

Difficulty: 🟢 Easy
Topics: collections.Counter, most_common(), dict sorting, character frequency

Author: @rampal-punia
"""

from collections import Counter


def analyze_character_frequency(text: str, top_n: int = 3) -> dict[str, int]:
    """Count character frequencies, excluding spaces and punctuation.

    Args:
        text: The string to analyze.
        top_n: Number of most common characters to highlight.

    Returns:
        Dictionary of all character counts (alphabetically sorted).
    """
    # Filter out non-alpha characters for a clean count
    cleaned = "".join(c for c in text.lower() if c.isalpha())
    counts = Counter(cleaned)

    print(f"  Text: '{text}'")
    print(f"  All counts: {dict(counts)}")
    print(f"  Top {top_n} most common: {counts.most_common(top_n)}")

    # Sort alphabetically
    sorted_counts = dict(sorted(counts.items()))
    print(f"  Sorted A-Z: {sorted_counts}")

    return sorted_counts


if __name__ == "__main__":
    print("── Character Frequency Analysis ──\n")
    analyze_character_frequency("I love learning Python a Lot", top_n=3)

# For more on Python follow: https://x.com/rs_punia_
