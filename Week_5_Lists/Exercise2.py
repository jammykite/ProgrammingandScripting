"""write a program that creates a random list of length 500 containing integers from 125 to 2250"""

import random

# Generate a random list of 500 integers between 125 and 2250
random_list = [random.randint(125, 2250) for _ in range(500)]

# Print the list
print("Random list of 500 integers:")
print(random_list)

# Find all numbers divisible by 5
divisible_by_5 = [num for num in random_list if num % 5 == 0]

# Print the numbers divisible by 5
print("Numbers divisible by 5:")
print(divisible_by_5)

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(num**0.5) + 1):  # Check divisors up to sqrt(num)
        if num % i == 0:
            return False
    return True

# Find all prime numbers in the list
prime_numbers = [num for num in random_list if is_prime(num)]

# Print the prime numbers
print("Prime numbers in the list:")
print(prime_numbers)

# Find all even numbers in the list
even_numbers = [num for num in random_list if num % 2 == 0]

# Print the even numbers
print("Even numbers in the list:")
print(even_numbers)

# Find all numbers divisible by both 2 and 10
divisible_by_2_and_10 = [num for num in random_list if num % 2 == 0 and num % 10 == 0]

# Print the numbers divisible by both 2 and 10
print("Numbers divisible by both 2 and 10:")
print(divisible_by_2_and_10)