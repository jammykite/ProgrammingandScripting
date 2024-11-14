""" Question 1: Given a list of ages below, write a function that calculates the average age of a person
Question 2: Write a function that takes in two arguments (number of hours worked and hourly rate) to compute the pay of an employee"""

"""list_of_ages = [20,21,24,13,15,19.22]
1. add all ages together
2. get number of ages
3. take the sum from 1. and divide it by output in 2.
4. return the output vaule in 3.
"""

def average_age(ages_list:list):
    """

    :param ages_list: should be a list of ages, expecting the data type to be a list
    :return: average age in float
    """
    sum_ages = sum(ages_list) #This will give us the sum of the ages
    num_ages = len(ages_list) #Get the number of ages in the list
    avg_list = sum_ages/num_ages #This is the avergae age
    return avg_list

list_ages_1 = [20,21,24,13,15,19.22]
average_age = average_age(list_ages_1)
print(f'The average age is {average_age}')


