while True:
    # Get user input
    input_string = input("Enter a sentence (or type 'exit' to quit): ")

    # Check if the user wants to exit
    if input_string.lower() == 'exit':
        break

    # Split the string into words
    words = input_string.split()

    # Find the length of the longest word
    max_length = max(len(word) for word in words)

    # Find all words with the maximum length
    longest_words = [word for word in words if len(word) == max_length]

    # Print the result
    print("The longest word(s) are:", ', '.join(longest_words))

