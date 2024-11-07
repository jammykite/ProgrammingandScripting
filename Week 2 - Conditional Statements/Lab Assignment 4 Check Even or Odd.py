"""
Write a function called is_even that takes a single integer as a parameter and returns True if the number is even
and False if it is odd

Use a lambda function to accomplish the same task and verify that both methods give the same result
"""

"""
1. ask user to enter an integer
2. use if else statements to define odd or even number
3. if number is even print true, if number is odd print false 
"""

# Define the is_even function
def is_even(number):
    return number % 2 == 0

# Define the lambda function for the same task
is_even_lambda = lambda number: number % 2 == 0

# Request user input
user_input = int(input("Enter a number: "))

# Check if the number is even using both methods
result_function = is_even(user_input)
result_lambda = is_even_lambda(user_input)

# Display the results
print(f"Using function: {user_input} is even? {result_function}")
print(f"Using lambda: {user_input} is even? {result_lambda}")

# Verify that both methods give the same result
if result_function == result_lambda:
    print("Both methods return the same result.")
else:
    print("The methods return different results.")
