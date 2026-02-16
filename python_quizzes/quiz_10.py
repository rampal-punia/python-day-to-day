"""Quiz 10: set.remove() vs set.discard().

Difficulty: 🟡 Intermediate
Topics: set.remove(), set.discard(), KeyError

Question: Which method raises an error if the element is not found?
    A) Only remove() raises KeyError
    B) Only discard() raises KeyError
    C) Both raise KeyError
    D) Neither raises an error
"""


def quiz() -> None:
    """remove() raises KeyError; discard() silently does nothing."""
    languages = {"Python", "Java", "JavaScript", "C++", "Ruby"}

    print("── Quiz 10 ──")
    print(f"  Original set: {languages}")

    # discard() — safe, no error if missing
    languages.discard("Ruby")
    print(f"  After discard('Ruby'): {languages}")

    languages.discard("Go")  # No error even though 'Go' not in set
    print(f"  After discard('Go'):   {languages} (no error)")

    # remove() — raises KeyError if missing
    languages.remove("Java")
    print(f"  After remove('Java'):  {languages}")

    try:
        languages.remove("Go")  # KeyError!
    except KeyError as e:
        print(f"  remove('Go'):          KeyError: {e}")

    # Answer: A) Only remove() raises KeyError
    print("\n  remove()  → raises KeyError if element is absent")
    print("  discard() → does nothing if element is absent")


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
