"""
Write a program that prompts the user for a number and checks if the number is prime.
o A prime number is only divisible by 1 and itself.
o Use a for loop to test for factors from 2 up to the number itself.
o If the number is prime, print "The number is prime".
o Otherwise, print "The number is not prime"
"""

"""
Step One: Ask user to input a number
Step Two: Check if the number is a prime number
Step Three: Print the result
"""

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(num**0.5) + 1):  # Check divisors up to sqrt(num)
        if num % i == 0:
            return False
    return True
#While loop allows user to try again if number is not prime
while True:
    # Ask user to input a number
    user_input = int(input("Please enter a number to check if it is a prime number: "))

    # Check if user input is a prime number
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
        break  # Exit the loop if the number is prime
    else:
        print(f"{user_input} is not a prime number. Try again!")