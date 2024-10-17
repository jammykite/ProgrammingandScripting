First_name=input("Please enter your first name: ")
Last_name=input("Please enter your last name: ")

Full_name=First_name+" "+Last_name

name_title = Full_name.title()
print(f"Your full name is: {name_title}")

lower_case = Full_name.lower()
print(f"if I whisper it sounds like: {lower_case}")

upper_case = Full_name.upper()
print(f"but if I yell!, it sounds like: {upper_case}")

reverse_word = Full_name[::-1]
print(f"in reverse your name is: {reverse_word.title()}")

