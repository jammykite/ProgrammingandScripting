"""
Write a function that takes a tuple of numbers as an argument and
returns a new tuple with the elements in ascending order.
You should not use the built-in sort or sorted functions. For example:
"""
# Defne a function for sorting a tuple
# We will convert the tuple to a list
# We will traverse the list and compare elements

def sort_tuple(input_tuple):
    converted_tuple = list(input_tuple)
    for i in range(len(converted_tuple)):
        for j in range(i + 1, len(converted_tuple)):
            if converted_tuple[i] > converted_tuple[j]:
                converted_tuple[i], converted_tuple[j] = converted_tuple[j], converted_tuple[i]
    return tuple(converted_tuple)

if __name__ == '__main__':
    """
    input_tuple = (2, 3, 1, 2, 7, 10, 9)
    input_tuple = [2, 3, 1, 2, 7, 10, 9]
    input_tuple_list = [2, 3, 1, 2, 7, 10, 9] 
    """
    input_tuple = (2, 3, 1, 2, 7, 10, 9)
    print(f'The original tuple is: {input_tuple}')
    print(f'The sorted tuple is: {sort_tuple(input_tuple)}')



