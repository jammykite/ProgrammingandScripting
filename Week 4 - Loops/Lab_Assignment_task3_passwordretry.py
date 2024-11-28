"""
• Write a program that asks the user to enter a password.
• If the password is incorrect, allow the user up to three attempts to try again.
• If the user enters the correct password within three attempts, print "Access • If they fail to enter the correct password after three attempts, print "Access granted".
denied".
"""

"""
Step One: Ask user to input their password
Step Two: check if user input matches stored password
Step Three: 
Step Four: if user input is incorrect, give 3 total attempts to try again
"""

# Predefined correct password
correct_password = "Password123"

# Allow up to three attempts
for attempt in range(1, 4):
    # Ask user to enter their password
    user_input = input("Enter your password: ")

    # Check if the password matches
    if user_input == correct_password:
        print("Logged in successfully")
        break
    else:
        print(f"Incorrect password. You have {3 - attempt} attempts left")
else:
    # If no attempts left
    print("Account blocked, please contact your administrator")
