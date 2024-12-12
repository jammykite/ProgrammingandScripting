"""
Write a function that calculates the sum of all
even numbers from 1 to a user-provided number n.

"""
import random


def sum_even_num(user_provided_num):
    """

    :param user_provided_num: user provided integer num
    :return: sum of numbers in int/whole number
    """
    sum_even = 0
    for i in range(0, user_provided_num+1, 2):
        if i == 0:
            continue
        else:
            sum_even +=i
        print(i)
        print(f'Sum of even at {i} is {sum_even}')
    print(f'The sum of even number between 1 and {user_provided_num} is {sum_even}')

"""
•	Write a program that simulates a number guessing game.
o	The program should pick a random number between 1 and 10.
o	The user has five attempts to guess the number.
o	If the user guesses correctly, print "Congratulations! You guessed it right!".
o	If the guess is too high or too low, give a hint.
o	End the game early if the user guesses correctly or runs out of attempts.

"""
def guess_game():
    computer_guess = random.choice([i for i in range(1, 11)])
    print(f'Computer Picked {computer_guess}!')
    num_trial = 0
    while num_trial <= 5:
        user_guess = int(input(f'Please enter your guess here: '))
        if computer_guess == user_guess:
            print(f'Congratulations! you guessed it right!')
            break

        elif computer_guess < user_guess:
            print(f'You have entered a number greater than the computer guess by at least {user_guess-computer_guess-1}')
            num_trial +=1
            continue
        elif computer_guess > user_guess:
            print(
                f'You have entered a number less than the computer guess by at least {computer_guess - user_guess - 1}')
            num_trial +=1
            continue




if __name__ == '__main__':
    guess_game()
    # sum_even_num(20)