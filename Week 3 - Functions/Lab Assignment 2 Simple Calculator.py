"""
Write a function called calculate that takes three parameters: num1, num2 and operation

The operation parameter should be a string: either "add", "subtract", "Multiply", or '"divide"

The function should return the result based on the operation specified.

Add a lambda function for each operation and verify the output matches the function results.
"""

"""
1. define calculate function
2. use if and elif statements to define operations including division by 0
3. ask user to input two numbers and select their operator
4. print result 
"""

# Define the calculate function
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        raise 6
        "Invalid operator"

# Lambda functions for each operation
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: "Error: Cannot divide by zero" if y == 0 else x / y
}

# Ask user for input
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
operation = input("Operator (+, -, *, /): ")

# Calculate using the function
result_function = calculate(num1, num2, operation)

# Calculate using the lambda functions in the dictionary
if operation in operations:
    result_lambda = operations[operation](num1, num2)
else:
    result_lambda = "Invalid operation"

# Print results to verify they match
print("Result using function:", result_function)
print("Result using lambda:", result_lambda)

