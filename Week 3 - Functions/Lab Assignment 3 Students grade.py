"""
Write a program that takes in a students test score (out of 100) and returns their letter grade based on the following scale:
90-100=A
80-89=B
70-79=C
60-69=D
below 60 = F

Use a lambda function to validate whether a score is within the correct range (0-100). If the score is not valid, return "invalid Score"

"""

"""
1. Ask user to input their test score
2. use if and elif statements to define grade based on score
3. print grade
4. use lambda function to validate that score is within correct range
5. if score not in correct range, print 'invalid score'
"""

# Lambda function to check if score is in the range 0-100
is_valid_score = lambda score: 0 <= score <= 100

while True:
    # Request user to enter their test score
    test_score = int(input('Please enter your test score (0 - 100): '))

    # Validate the score using the lambda function
    if not is_valid_score(test_score):
        print('Invalid score. Please enter a score between 0 and 100.')
        continue  # Ask for input again if the score is out of range

    # Define grades based on user's input
    if 90 <= test_score <= 100:
        print('Your grade is an A, Well done!')
    elif 80 <= test_score < 90:
        print('Your grade is a B, Great job!')
    elif 70 <= test_score < 80:
        print('Your grade is a C, Good effort!')
    elif 60 <= test_score < 70:
        print('Your grade is a D, Keep trying!')
    elif 0 <= test_score < 60:
        print('Your grade is an F, Don’t give up!')

