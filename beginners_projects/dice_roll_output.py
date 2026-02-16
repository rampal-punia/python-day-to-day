"""Dice Roll Outcomes — Simulating dice rolls using Python's random module.

Difficulty: 🟢 Easy
Topics: random module, functions, f-strings, type hints

Author: @rampal-punia
"""

import random


# ── 🟢 Easy: Basic Dice Roll ────────────────────────────────────────


def roll_single_die() -> int:
    """Roll a single six-sided die and return the result (1-6)."""
    return random.randint(1, 6)


def roll_with_choice() -> int:
    """Roll a die using random.choice on a tuple of outcomes."""
    outcomes = (1, 2, 3, 4, 5, 6)
    return random.choice(outcomes)


# ── 🟡 Intermediate: Multiple Dice & Statistics ─────────────────────


def roll_multiple_dice(num_dice: int = 2) -> list[int]:
    """Roll multiple dice and return a list of results.

    Args:
        num_dice: Number of dice to roll (default: 2).

    Returns:
        A list of integers, each between 1 and 6.

    Raises:
        ValueError: If num_dice is less than 1.
    """
    if num_dice < 1:
        raise ValueError("Must roll at least 1 die")
    return [random.randint(1, 6) for _ in range(num_dice)]


def roll_statistics(num_rolls: int = 1000) -> dict[int, int]:
    """Roll a die many times and return the frequency distribution.

    Args:
        num_rolls: Number of times to roll the die.

    Returns:
        Dictionary mapping each face (1-6) to its count.
    """
    counts: dict[int, int] = {face: 0 for face in range(1, 7)}
    for _ in range(num_rolls):
        counts[roll_single_die()] += 1
    return counts


# ── 🔴 Advanced: Loaded Dice with Weighted Probabilities ────────────


def roll_loaded_die(weights: tuple[int, ...] = (1, 1, 1, 1, 1, 5)) -> int:
    """Roll a loaded (weighted) die using random.choices.

    Args:
        weights: Relative weights for faces 1-6. Higher = more likely.

    Returns:
        The face that landed (1-6).
    """
    faces = (1, 2, 3, 4, 5, 6)
    return random.choices(faces, weights=weights, k=1)[0]


if __name__ == "__main__":
    print("── 🟢 Easy: Single Die Rolls ──")
    print(f"  roll_single_die()  → {roll_single_die()}")
    print(f"  roll_with_choice() → {roll_with_choice()}")

    print("\n── 🟡 Intermediate: Multiple Dice ──")
    results = roll_multiple_dice(5)
    print(f"  Rolling 5 dice → {results}  (sum={sum(results)})")

    print("\n── 🟡 Frequency Distribution (1000 rolls) ──")
    stats = roll_statistics(1000)
    for face, count in sorted(stats.items()):
        bar = "█" * (count // 10)
        print(f"  Face {face}: {count:>4} times  {bar}")

    print("\n── 🔴 Advanced: Loaded Die (face 6 is 5x more likely) ──")
    loaded_stats: dict[int, int] = {f: 0 for f in range(1, 7)}
    for _ in range(1000):
        loaded_stats[roll_loaded_die()] += 1
    for face, count in sorted(loaded_stats.items()):
        bar = "█" * (count // 10)
        print(f"  Face {face}: {count:>4} times  {bar}")

# For more on Python follow: https://x.com/rs_punia_
