while True:
    StudentNumber = input('Enter your Student Number: ')
    if StudentNumber == '50103233':
        print(StudentNumber, 'Student found')
        password = input('Enter your password: ')
        if password == 'password':
            print('Password correct. Access granted.')
            break
        else:
            print('Incorrect password. Try again.')
    else:
        print(StudentNumber, 'not found')
