"""Random Choice — Pick random items from a sequence.

Difficulty: 🟢 Easy
Topics: random.choice, random.choices, random.sample

random.choice(seq)       → Pick ONE random item
random.choices(seq, k=n) → Pick n items WITH replacement
random.sample(seq, k=n)  → Pick n items WITHOUT replacement

Author: @rampal-punia
"""

import random


def demo_random_choice() -> None:
    """Demonstrate different ways to pick random items."""
    options = ["Python Coding", "Outing", "Movie", "Songs"]

    print("── random.choice (one item) ──")
    for i in range(5):
        pick = random.choice(options)
        print(f"  Attempt {i + 1}: {pick}")

    print("\n── random.choices (k items, with replacement) ──")
    picks = random.choices(options, k=3)
    print(f"  3 picks: {picks}")

    print("\n── random.sample (k items, without replacement) ──")
    unique_picks = random.sample(options, k=3)
    print(f"  3 unique picks: {unique_picks}")

    # Weighted choices
    print("\n── Weighted random.choices ──")
    weights = [0.5, 0.2, 0.2, 0.1]  # Python Coding is 50% likely
    weighted = random.choices(options, weights=weights, k=10)
    print(f"  Weights: {dict(zip(options, weights))}")
    print(f"  10 picks: {weighted}")


if __name__ == "__main__":
    demo_random_choice()

# For more on Python follow: https://x.com/rs_punia_
