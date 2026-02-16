"""Generators 05 — State management: generators remember where they left off.

Difficulty: 🟡 Intermediate
Topics: generator state, pause/resume, local variable preservation

Unlike regular functions that start fresh on every call, generators
PAUSE at each `yield` and RESUME from exactly that point when `next()`
is called again. All local variables are preserved between calls.

This makes generators ideal for:
    - Coroutines and cooperative multitasking
    - Stateful iteration (e.g., reading a file line by line)
    - Pause/resume patterns (like this countdown demo)

Author: @rampal-punia
"""

from typing import Generator


def countdown(n: int) -> Generator[int, None, None]:
    """Count down from n to 1, preserving state between calls.

    Each call to next() resumes where the previous yield paused.
    The local variable `n` is preserved across calls.

    Args:
        n: The number to count down from.

    Yields:
        Integers from n down to 1.
    """
    print(f"  [countdown] Starting from {n}")
    while n > 0:
        yield n
        n -= 1
    print("  [countdown] Finished!")


def id_generator(prefix: str = "ID") -> Generator[str, None, None]:
    """Generate unique sequential IDs — state (counter) never resets.

    Args:
        prefix: String prefix for each ID.

    Yields:
        Strings like 'ID-001', 'ID-002', etc.
    """
    counter = 0
    while True:
        counter += 1
        yield f"{prefix}-{counter:03d}"


if __name__ == "__main__":
    # ── Pause and Resume demo ──
    print("── Countdown: Pause & Resume ──")
    gen = countdown(5)

    print(f"  next → {next(gen)}")  # 5
    print(f"  next → {next(gen)}")  # 4
    print(f"  next → {next(gen)}")  # 3

    print("\n  ... doing something else (generator is paused) ...\n")

    print(f"  next → {next(gen)}")  # 2  (resumes right where it left off)
    print(f"  next → {next(gen)}")  # 1

    # Exhaustion
    try:
        next(gen)
    except StopIteration:
        print("  StopIteration caught — countdown exhausted.")

    # ── Stateful ID generator ──
    print("\n── Stateful ID Generator ──")
    ids = id_generator("USER")
    for _ in range(5):
        print(f"  {next(ids)}")

    print("  ... pause ...")
    # Counter is preserved — next ID continues from 6, not 1
    for _ in range(3):
        print(f"  {next(ids)}")
