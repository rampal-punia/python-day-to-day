"""Random RGB Colors — Generate random RGB tuples.

Difficulty: 🟢 Easy
Topics: random.randint, random.sample, tuple, RGB colors

Author: @rampal-punia
"""

import random


def random_rgb_randint() -> tuple[int, int, int]:
    """Generate a random RGB color using randint."""
    return tuple(random.randint(0, 255) for _ in range(3))  # type: ignore


def random_rgb_sample() -> tuple[int, int, int]:
    """Generate a random RGB color using sample (all 3 values unique)."""
    return tuple(random.sample(range(256), 3))  # type: ignore


if __name__ == "__main__":
    print("── Random RGB Colors ──")
    print(f"  Method 1 (randint): {random_rgb_randint()}")
    print(f"  Method 2 (sample):  {random_rgb_sample()}")

    print("\n  5 random colors:")
    for i in range(5):
        rgb = random_rgb_randint()
        print(f"    #{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}  RGB{rgb}")

# For more on Python follow: https://x.com/rs_punia_
