'''Python: Rock, Paper Scissors Game. Can be used for Water, Snake, Gun game also.'''

import random


def game(choice1, choice2, choice3):
    """Play a game of rock-paper-scissors (or any other 3-choice game)"""

    print(f"Let's play {choice1}, {choice2}, {choice3}")
    choices = (choice1, choice2, choice3)

    user_choice = input(
        f"Enter your choice ({choice1}/{choice2}/{choice3}): ").capitalize()
    if user_choice not in choices:
        print("Invalid choice!")
        return

    computer_choice = random.choice(choices)
    print(f"🤖 Computer: {computer_choice}, 🙋 You: {user_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!!!")
    elif(
        (user_choice == choice1 and computer_choice == choice2) or
        (user_choice == choice2 and computer_choice == choice3) or
        (user_choice == choice3 and computer_choice == choice1)
    ):
        print("🤖 Computer Wins")
    else:
        print("🙋 You Win")


while True:
    game("Rock", "Paper", "Scissors")
    # game("Water", "Snake", "Gun")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break
