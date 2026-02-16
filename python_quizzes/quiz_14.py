"""Quiz 14: String slicing — reverse with [::-1].

Difficulty: 🟢 Easy
Topics: string slicing, step parameter, reversal

Question: What is the output of "I love Python"[::-1]?
    A) n
    B) nohtyP evol I
    C) Error
"""


def quiz() -> None:
    """[::-1] creates a reversed copy of the string."""
    text = "I love Python"
    reversed_text = text[::-1]

    print("── Quiz 14 ──")
    print(f"  '{text}'[::-1] = '{reversed_text}'")
    # Answer: B) nohtyP evol I
    # [::-1] means start:stop:step with step=-1 (reverse)


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
