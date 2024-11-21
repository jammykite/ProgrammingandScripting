"""
Your second task is to build a chatbot for MoodSense, a company that offers mental wellness solutions.
You need to develop a chatbot that asks users to describe their mood on a scale of 1 to 10 and provides
an appropriate response based on their input.

The response flow should follow this logic:
•	1-3: “I’m sorry you’re feeling this way. Consider talking to a friend or taking some time for yourself.”
•	4-7: “It seems like you're having an okay day. Remember to take breaks and focus on self-care.”
•	8-10: “That’s great to hear! Keep up the positive energy!”
"""

"""
Step One: Ask user to input an integer from 1-10
Step Two: Determine output message based on users input
Step Three: Print output
"""
# Print introduction text
print("Welcome to MoodSense! We offer mental wellness solutions")
users_name = input("Please tell me your name: ") #ask users name to personalise responses
print(f"Hi {users_name.title()}")
#Request that user input their mood using an integer from 1-10
while True:  # Start a loop, this will prompt user to re-enter their input if non integer is entered
    mood_input = input("Please tell me your current mood using a scale from 1-10 with 1 being a bad mood and 10 being the best: ")
    # Check if the input is an integer from 1-10
    if mood_input.isdigit():
        mood_input = int(mood_input)  # convert user input to an integer, this will be used to determine response
        if 1 <= mood_input <= 10:  # Check if user input is 1-10
            break  # Exit the loop if input is valid
        else:
            print("Invalid input. Please tell me your current mood using a scale from 1-10.") #response if integer larger than 10 is entered
    else:
     