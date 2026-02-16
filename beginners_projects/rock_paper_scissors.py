"""Rock, Paper, Scissors — A 3-choice game with score tracking.

Difficulty: 🟢 Easy → 🟡 Intermediate (score tracking, best-of-N)
Topics: random, tuples, conditionals, f-strings, type hints

Supports any 3-choice game where choice1 beats choice3,
choice2 beats choice1, and choice3 beats choice2 (circular wins).

Author: @rampal-punia
"""

import random


def determine_winner(user: str, computer: str, choices: tuple[str, str, str]) -> str:
    """Determine the winner of a single round.

    Win logic (circular): choice[0] beats choice[2],
    choice[1] beats choice[0], choice[2] beats choice[1].

    Args:
        user: The user's choice.
        computer: The computer's choice.
        choices: Tuple of the 3 valid choices in order.

    Returns:
        "tie", "user", or "computer".
    """
    if user == computer:
        return "tie"

    # Define who beats whom (circular: each beats the previous)
    beats = {
        choices[0]: choices[2],  # Rock beats Scissors
        choices[1]: choices[0],  # Paper beats Rock
        choices[2]: choices[1],  # Scissors beats Paper
    }

    return "user" if beats[user] == computer else "computer"


def play_round(choices: tuple[str, str, str]) -> str:
    """Play a single round of the game.

    Args:
        choices: Tuple of the 3 valid choices.

    Returns:
        "tie", "user", or "computer", or "invalid".
    """
    prompt = f"Enter your choice ({'/'.join(choices)}): "
    user_choice = input(prompt).strip().capitalize()

    if user_choice not in choices:
        print(f"  ❌ Invalid choice! Must be one of: {', '.join(choices)}")
        return "invalid"

    computer_choice = random.choice(choices)
    print(f"  🤖 Computer: {computer_choice}  |  🙋 You: {user_choice}")

    result = determine_winner(user_choice, computer_choice, choices)

    if result == "tie":
        print("  🤝 It's a Tie!")
    elif result == "user":
        print("  🎉 You Win!")
    else:
        print("  💻 Computer Wins!")

    return result


def play_game(
    choices: tuple[str, str, str] = ("Rock", "Paper", "Scissors"),
    best_of: int = 3,
) -> None:
    """Play a best-of-N match with score tracking.

    Args:
        choices: Tuple of the 3 valid choices.
        best_of: Number of rounds to play (default: 3).
    """
    wins_needed = best_of // 2 + 1
    user_score = 0
    computer_score = 0

    print(f"\n{'═' * 45}")
    print(f"  🎮 {choices[0]}, {choices[1]}, {choices[2]} — Best of {best_of}")
    print(f"{'═' * 45}")

    round_num = 0
    while user_score < wins_needed and computer_score < wins_needed:
        round_num += 1
        print(f"\n── Round {round_num} ──")
        result = play_round(choices)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        # ties and invalid don't count

        print(f"  Score → You: {user_score}  |  Computer: {computer_score}")

    print(f"\n{'─' * 45}")
    if user_score > computer_score:
        print(f"  🏆 You win the match {user_score}-{computer_score}!")
    else:
        print(f"  💻 Computer wins the match {computer_score}-{user_score}!")


if __name__ == "__main__":
    while True:
        play_game()
        # Also works for Water/Snake/Gun:
        # play_game(("Water", "Snake", "Gun"))
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! 👋")
            break

# For more on Python follow: https://x.com/rs_punia_
