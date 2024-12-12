"""
Write a program that asks the user for STID,
if the student ID is on record, proceed to ask for their password
if the password is on record, then proceed to print out, you have beenlogged in!

"""

def check_user_password():
    student_IDs = ['12325', '456781', '23456', '123456']
    student_passwords = ['password123', 'password', 'passwd', 'PASSWORDANGEL']
    num_times_pass = 0
    while num_times_pass <= 3:
        user_input = input(f'Please enter your student ID here, e.g 1234567: ')
        num_times_pass +=1
        if user_input in student_IDs and num_times_pass <3:
            student_psswd = input(f'Please enter your password here: ')
            if student_psswd in student_passwords:
                print(f'You have been logged in\n Welcome Back!')
                break
            else:
                print(f'You have entered the wrong password, please try again!')
        # elif user_input not in student_IDs and num_times_pass < 3:
        #     continue

        else:
            print(f'You have entered the wrong Student ID!, please try again')

if __name__ == '__main__':
    check_user_password()