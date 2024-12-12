"""
Write a function that takes a tuple of integers as an argument and returns
the product of all the elements in the tuple. For example:
product(1, 2, 3) returns 6
product(4, 0, 2) returns 0
"""

# Define a function to calculate the product of all elements in a tuple
# We will initialize the result to 1
# Traverse the tuple and multiply all elements
# Return the result

def product_tuple(number_tuple):
    """
    This function takes a tuple of integers as an argument and returns the product of all the elements in the tuple.
    :param number_tuple: tuple of integers
    :return: product of all elements in the tuple
    """
    res = 1
    for int_num in number_tuple: # Traverse the tuple
        res *= int_num #iteratively multiply all elements
    return res

if __name__ == '__main__':
    input_tuple_1 = (1, 2, 3, 2, 1, 2, 3, 4, 5, 1, 7, 8, 4, 2, 3, 67, 8, 22)
    input_tuple_2 = (4, 0, 2, 21, 2, 3, 4, 5, 6, 7, 1)
    print(f'The product of all elements in the tuple {input_tuple_1} is: {product_tuple(input_tuple_1)}')
    print(f'The product of all elements in the tuple {input_tuple_2} is: {product_tuple(input_tuple_2)}')