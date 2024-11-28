"""Write a program that simulates a number guessing game.

The program should pick a random number between 1 and 10.

The user has five attempts to guess the number.

If the user guesses correctly, print "Congratulations! You guessed it right!".

If the guess is too high or too low, give a hint.

End the game early if the user guesses correctly or runs out of attempts."""

"""
Step 1: CPU picks a random number from 1-10
Step 2: ask for users input
Step 3: if users input matches CPU number, user is right
Step 4: if users input is incorrect, give a hint
"""

import random

def number_guessing_game():
    # Generate a random number between 1 and 10
    CPU_number = random.randint(1, 10)
    attempts = 5  # User has 5 attempts

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 10. Can you guess what it is? You have 5 attempts.")

    for attempt in range(1, attempts + 1):
        try:
            # Get the user's guess
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))

            # Check the user's guess
            if guess == CPU_number:
                print("Congratulations! You guessed it right!")
                break
            elif guess < CPU_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 10.")

        # If the user runs out of attempts
        if attempt == attempts:
            print(f"Sorry, you're out of attempts. The number was {CPU_number}. Better luck next time!")

# Start the game
if __name__ == '__main__':
    number_guessing_game()
