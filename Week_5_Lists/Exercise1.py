"""Write a program that asks for user input and calculates the sum of all numbers from 1 to the entered number"""

"""
Step 1 - ask user to input a number
Step 2 - calculate the sum of all numbers from 1 to the entered number
Step 3 - print result
"""

user_input = int(input('Please enter a whole number: '))

total_sum = user_input * (user_input + 1) //2
print(total_sum)