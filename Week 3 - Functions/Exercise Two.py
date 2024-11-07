""" Question 1: Given a list of ages below, write a function that calculates the average age of a person
Question 2: Write a function that takes in two arguments (number of hours worked and hourly rate) to compute the pay of an employee"""

"""
1. Ask the user for their hourly rate
2. Ask the user for the number of hours worked
3. Multiply 1. and 2. to get the pay of the employee
4. Return the value in 3.
"""

def employee_pay():
    """
    :return: the employee pay in float in currency £
    """

    hourly_rate = float(input("Please enter hourly rate eg 10.59: "))
    num_hours_worked = float(input("Please enter number of hours worked eg 21.5: "))
    emp_pay = hourly_rate * num_hours_worked
    emp_pay = f'£{emp_pay: }'
    return emp_pay

# Test employee pay code

emp_pay = employee_pay()
print (f'Employee pay is {emp_pay}')




