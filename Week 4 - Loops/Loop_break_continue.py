tries = 0  # Initialize counter for password attempts

while True:
    StudentNumber = input('Enter your Student Number: ')
    if StudentNumber == '50103233':
        print(StudentNumber, 'Student found')

        # Loop for password attempts
        while tries < 3:
            password = input('Enter your password: ')
            if password == 'password':
                print('Password correct. Access granted.')
                break
            else:
                tries += 1
                print(f'Incorrect password. Try again. ({3 - tries} attempts left)')
                if tries < 3:
                    continue  # Go back to the start of the password loop
                else:
                    print("Too many incorrect attempts. Access denied.")
                    break
        break  # Break the main loop if access granted or attempts exhausted
    else:
        print(StudentNumber, 'not found')
