import random

game_message = '''
Let's play Higher or Lower.
Computer will guess a number between 1-100.
You have to guess the correct number in 8 attempts to win the game.
The computer will give feed-back as 'higher or lower' for user's input.
'''
print(game_message)


def validate_input(user_input):
    try:
        user_input = int(user_input)
        if user_input < 1 or user_input > 100:
            raise ValueError("Number must be between 1 and 100")
        return user_input
    except ValueError:
        print("Input must be a number between 1 and 100!!!")
        print("Exiting the game!!!")
        return None


def run():
    computer_choice = random.randint(1, 100)
    user_guess = input("Enter a number (1 and 100): ")
    user_guess = validate_input(user_guess)
    if user_guess:
        count = 1
        while user_guess != computer_choice and count < 8:

            if user_guess < computer_choice:
                print("Higher than this")
            elif user_guess > computer_choice:
                print("Lower than this")

            print(f"Number of attempts: {count}")
            user_guess = input("Enter a number (1 and 100): ")
            user_guess = validate_input(user_guess)
            if user_guess:
                count += 1
            else:
                break

        print(f"The computer guessed the number {computer_choice}")
        if user_guess == computer_choice:
            print(f"Congratulations, You Won in {count} attempts!!!")
        else:
            print(f"Computer win. You attempted {count} times!!!")


def play_game():
    while True:
        run()
        is_play_again = input("Do you want to play again? (y/n): ")
        if is_play_again.lower() != 'y':
            break


play_game()
