First_name=input("Please enter your first name: ")
Last_name=input("Please enter your last name: ")

Full_name=First_name.title() +" "+ Last_name.title()

print(f"If I say your name 3 times in a mirror you might appear, Here goes... {', '.join([Full_name] * 3)} ..Did it work?")