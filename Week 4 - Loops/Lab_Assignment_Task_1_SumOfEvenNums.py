"""
Write a program that calculates the sum of all even numbers from 1 to a user-provided number n.
"""
"""
1. Request that user enters a number
2. find the even numbers from 1 to users entered number
3. calculate sum of all even numbers
4. print result
"""
#Request that user enter their number
n = int(input('Please enter your number:'))
# Find all even numbers from 1 to n
even_numbers = [i for i in range(1, n + 1) if i % 2 == 0]

# Calculate the sum of all even numbers
sum_of_evens = sum(even_numbers)

# Print the result
print(f"The sum of all even numbers from 1 to {n} is: {sum_of_evens}")

