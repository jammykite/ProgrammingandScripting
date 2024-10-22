def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_string = ''.join(s.split()).lower()
    # Check if the string is the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

# Get user input
print("Welcome to the Palindrome Tester!\n")
user_input = input("Please enter a word to see if it is a palindrome: ")

# Check if it is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
