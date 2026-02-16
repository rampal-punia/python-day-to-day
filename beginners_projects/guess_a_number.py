"""Guess a Number — Higher or Lower game with input validation.

Difficulty: 🟢 Easy
Topics: random, input validation, while loop, f-strings

Rules:
    - Computer picks a random number between 1 and 100.
    - Player has 8 attempts to guess it.
    - After each guess, the computer hints "Higher" or "Lower".

Author: @rampal-punia
"""

import random


def validate_input(user_input: str) -> int | None:
    """Validate that user_input is an integer between 1 and 100.

    Args:
        user_input: The raw string from the user.

    Returns:
        The integer value if valid, or None if invalid.
    """
    try:
        value = int(user_input)
        if not 1 <= value <= 100:
            raise ValueError("Number must be between 1 and 100")
        return value
    except ValueError:
        print("⚠️  Input must be a number between 1 and 100!")
        return None


def run_game(max_attempts: int = 8) -> None:
    """Run a single round of the guessing game.

    Args:
        max_attempts: Maximum number of guesses allowed.
    """
    target = random.randint(1, 100)
    print(
        f"\n🎯 I've picked a number between 1 and 100. You have {max_attempts} attempts."
    )

    for attempt in range(1, max_attempts + 1):
        raw = input(f"  Attempt {attempt}/{max_attempts} — Enter your guess: ")
        guess = validate_input(raw)

        if guess is None:
            continue  # Invalid input — don't count as an attempt? Let's still increment.

        if guess == target:
            print(
                f"  🎉 Congratulations! You guessed {target} in {attempt} attempt(s)!"
            )
            return
        elif guess < target:
            print("  ⬆️  Higher than that!")
        else:
            print("  ⬇️  Lower than that!")

    print(f"  😞 Out of attempts! The number was {target}.")


def play() -> None:
    """Main game loop — allows replaying."""
    print("═" * 50)
    print("   🎲 GUESS A NUMBER — Higher or Lower Game")
    print("═" * 50)

    while True:
        run_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    play()
