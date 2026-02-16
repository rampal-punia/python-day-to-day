"""Extracting Substrings — 6 different methods to get 'is' from a string.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: index(), slicing, re.search(), split(), partition(), find()

Author: @rampal-punia
"""

import re


def extract_substring_demos() -> None:
    """Show 6 methods to extract 'is' from a string."""
    source = "Python is Awesome!!!"
    target = "is"

    print(f"  Source: '{source}'")
    print(f"  Target: '{target}'\n")

    # Method 1: Using index() — finds position, then slice
    idx = source.index(target)
    result = source[idx : idx + len(target)]
    print(f"  1. index() + slice:  '{result}'  (found at index {idx})")

    # Method 2: Using find() — like index() but returns -1 instead of raising
    idx = source.find(target)
    result = source[idx : idx + len(target)] if idx != -1 else "Not found"
    print(f"  2. find() + slice:   '{result}'  (found at index {idx})")

    # Method 3: Using re.search() — regex pattern matching
    match = re.search(target, source)
    result = match.group() if match else "Not found"
    print(
        f"  3. re.search():      '{result}'  (span={match.span() if match else 'N/A'})"
    )

    # Method 4: Using split() — split by space, pick by position
    words = source.split(" ")
    result = words[1]  # 'is' is the second word
    print(f"  4. split():          '{result}'  (words={words})")

    # Method 5: Using partition() — splits into (before, match, after)
    before, match_str, after = source.partition(target)
    print(
        f"  5. partition():      '{match_str}'  ('{before}' | '{match_str}' | '{after}')"
    )

    # Method 6: Using 'in' operator — boolean check (doesn't extract)
    found = target in source
    print(f"  6. 'in' operator:    found={found}")


if __name__ == "__main__":
    print("── 6 Ways to Extract a Substring ──\n")
    extract_substring_demos()

# For more on Python follow: https://x.com/rs_punia_
