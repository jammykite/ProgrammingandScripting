""""
Write a function called max_of_two that takes two numbers as parameters and returns the larger of the two.

Use a lambda function to achieve the same task and compare the results from both approaches.
"""

'''
1. Ask user to enter number 1
2. Ask user to enter number 2
3. Print larger number
'''

# Define the max_of_two function
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

# Define a lambda function to do the same thing
max_of_two_lambda = lambda x, y: x if x > y else y

# Ask user to enter numbers
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

# Get results from both approaches
result_function = max_of_two(num1, num2)
result_lambda = max_of_two_lambda(num1, num2)

# Print the results
print("Larger number using function:", result_function)
print("Larger number using lambda:", result_lambda)

