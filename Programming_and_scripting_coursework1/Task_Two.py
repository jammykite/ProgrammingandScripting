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
#Request that user input their mood using an integer from 1-10
mood_input = int(input("Please tell me your current mood using a scale from 1-10 with 1 being a bad mood and 10 being the best: "))
#IF, ELIF, ELSE statements to determine output based on users input
if 1 <= mood_input <= 3:
    print("I’m sorry you’re feeling this way. Consider talking to a friend or taking some time for yourself.")
elif 4 <= mood_input <= 7:
    print("It seems like you're having an okay day. Remember to take breaks and focus on self-care.")
elif 8 <= mood_input <= 10:
    print("That’s great to hear! Keep up the positive energy!")
else:
    print("Please enter a number between 1 and 10.")

