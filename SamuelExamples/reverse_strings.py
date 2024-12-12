"""
Write a program that:

Accepts a sentence from the user.

Splits it into words (use .split()).

Reverses the order of words.

Joins the words back into a sentence.

"""

def reverser_strings():
    """
    This function asks the user to input a sentence.
    Then reverses the order of the sentence.
    Returns: reversed sentence

    """
    'My name is David ==> David is name My'
    "['My', 'name', 'is', 'David'] ==>"
    sentence = input('Please enter a sentence you would like to reverse: ')
    words_list = sentence.split()
    print(f'Split sentence into words: {words_list}')
    # reversed_sentence = words_list[::-1]
    reversed_sentence = ' '.join(reversed(words_list))
    print(f'Reversed sentence: {reversed_sentence}')

if __name__ == '__main__':
    reverser_strings()