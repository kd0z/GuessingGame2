

#KogeeDozier
#CIS261
#Guessing Game
import random


def guessing_game():
    while True:
        try:
            limit = int(
                input("Enter the maximum number for the guessing range: "))
            if limit < 1:
                print("Please enter a number greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        number_to_guess = random.randint(1, limit)
        print(
            f"I have chosen a number between 1 and {limit}. Can you guess it?")

        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! {guess} is the correct number!")
                break

        play_again = input(
            "Would you like to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    guessing_game()
