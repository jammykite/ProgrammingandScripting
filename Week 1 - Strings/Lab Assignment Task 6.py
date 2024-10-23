print("Welcome to the Palindrome Tester!\n")
user_input = input("Please enter a word to see if it is a palindrome: ")

cleaned_string = ''.join(user_input.split()).lower()

if cleaned_string == cleaned_string[::-1]:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
