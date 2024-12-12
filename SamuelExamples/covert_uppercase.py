"""
Write a function that takes a tuple of strings
as an argument and returns a new tuple with all the strings converted to uppercase.
For example:
>>> to_uppercase(('hello', 'world'))
('HELLO', 'WORLD')
>>> to_uppercase(('how', 'are', 'you'))
('HOW', 'ARE', 'YOU')
"""
# Define a function to convert all strings in a tuple to uppercase
# Traverse the tuple and convert each string to uppercase

def covert_uppercase(input_tuple_strings):
    """
    This function takes a tuple of strings as an argument
    and returns a new tuple with all the strings converted to uppercase.
    Args:
        input_tuple_strings:

    Returns:

    """
    uppercase_wordslist = []
    for word in input_tuple_strings:
        upper_case_word = word.upper()
        uppercase_wordslist.append(upper_case_word)
        print(upper_case_word)
    return tuple(uppercase_wordslist)


if __name__ == '__main__':
    input_strings_tuple = ('hello', 'world')
    print(f'The original tuple is: {input_strings_tuple}')
    print(f'The tuple with all strings converted to uppercase is: {covert_uppercase(input_strings_tuple)}')