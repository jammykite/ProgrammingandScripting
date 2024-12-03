"""
Write a program that:
1. Accepts a sentence from the user.
2. Splits it into words (use .split()).
3. Reverses the order of words.
"""

def reverse_sentence():
    """Accept a sentence, split it into words, and reverse the word order."""
    sentence = input("Enter a sentence: ").strip()
    if sentence:
        words = sentence.split()  # Split the sentence into words
        reversed_words = words[::-1]  # Reverse the order of words
        reversed_sentence = ' '.join(reversed_words)  # Join words back into a sentence
        print(f"Reversed sentence: {reversed_sentence}")
    else:
        print("You didn't enter a sentence!")

# Run the program
if __name__ == '__main__':
    reverse_sentence()
