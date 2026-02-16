"""Python Keywords — List all reserved keywords in the current version.

Difficulty: 🟢 Easy
Topics: keyword module, kwlist, softkwlist, reserved words

Author: @rampal-punia
"""

import keyword
import sys


def show_keywords() -> None:
    """Display all Python keywords with their count."""
    kw_list = keyword.kwlist

    print(f"── Python {sys.version.split()[0]} Keywords ({len(kw_list)} total) ──")
    for i, kw in enumerate(kw_list, 1):
        print(f"  {i:>2}. {kw}")

    # Python 3.10+ has soft keywords (match, case, type, _)
    if hasattr(keyword, "softkwlist"):
        print(f"\n── Soft Keywords ({len(keyword.softkwlist)}) ──")
        for sk in keyword.softkwlist:
            print(f"  - {sk}")
        print("  (Soft keywords are context-dependent and can be used as names.)")

    # Check if a word is a keyword
    print("\n── Keyword Check ──")
    test_words = ["if", "return", "match", "hello", "class"]
    for word in test_words:
        print(f"  '{word}' is keyword: {keyword.iskeyword(word)}")


if __name__ == "__main__":
    show_keywords()
