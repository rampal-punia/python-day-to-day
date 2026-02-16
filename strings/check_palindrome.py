"""Palindrome Checker — Multiple approaches from basic to advanced.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: string slicing, recursion, two-pointer, deque, case handling

A palindrome reads the same forwards and backwards.
Examples: 'Rotator', 'racecar', 'A man a plan a canal Panama'

Author: @rampal-punia
"""

import re
from collections import deque


# ── 🟢 Method 1: Slicing (simplest) ──


def is_palindrome_slice(text: str) -> bool:
    """Check palindrome using string slicing [::-1].

    Args:
        text: The string to check.

    Returns:
        True if text is a palindrome (case-insensitive).
    """
    text = text.lower()
    return text == text[::-1]


# ── 🟢 Method 2: Two-pointer (no extra memory) ──


def is_palindrome_two_pointer(text: str) -> bool:
    """Check palindrome using two pointers converging from both ends."""
    text = text.lower()
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


# ── 🟡 Method 3: Recursive ──


def is_palindrome_recursive(text: str) -> bool:
    """Check palindrome recursively — compare outer chars, then recurse inward."""
    text = text.lower()
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome_recursive(text[1:-1])


# ── 🟡 Method 4: Deque (popleft + pop) ──


def is_palindrome_deque(text: str) -> bool:
    """Check palindrome using a deque — pop from both ends."""
    d = deque(text.lower())
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


# ── 🟡 Method 5: Phrase palindrome (ignoring spaces & punctuation) ──


def is_palindrome_phrase(text: str) -> bool:
    """Check if a phrase is a palindrome, ignoring non-alphanumeric characters.

    'A man, a plan, a canal: Panama!' → True
    """
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_words = ["click", "Rotator", "level", "Python", "racecar"]
    test_phrases = [
        "A man, a plan, a canal: Panama!",
        "Was it a car or a cat I saw?",
        "Hello, World!",
    ]

    print("── Word Palindromes ──")
    for word in test_words:
        results = {
            "slice": is_palindrome_slice(word),
            "two-ptr": is_palindrome_two_pointer(word),
            "recursive": is_palindrome_recursive(word),
            "deque": is_palindrome_deque(word),
        }
        status = "✅" if results["slice"] else "❌"
        print(f"  {status} '{word:12s}' → {results}")

    print("\n── Phrase Palindromes ──")
    for phrase in test_phrases:
        result = is_palindrome_phrase(phrase)
        status = "✅" if result else "❌"
        print(f"  {status} '{phrase}' → {result}")

# For more on Python follow: https://x.com/rs_punia_
