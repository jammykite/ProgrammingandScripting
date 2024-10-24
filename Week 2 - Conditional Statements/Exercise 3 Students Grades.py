while True:
 test_score=int(input('Please enter your test score 0 - 100: '))

 if (test_score <=100 and test_score >=90):
    print('Your grade is an A, Well done!')
 elif 80 <= test_score < 90:
    print('Your grade is a B, Great job!')
 elif 70 <= test_score < 80:
    print('Your grade is a C, Good effort!')
 elif 60 <= test_score < 70:
    print('Your grade is a D, Keep trying!')
 elif 0 <= test_score < 60:
    print('Your grade is an F, Don’t give up!')
 else:
    print('Invalid score. Please enter a score between 0 and 100.')
