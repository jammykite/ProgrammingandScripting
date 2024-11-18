""""
TASK 1 (35 Marks)
You are working as a software engineer for TechComp, a company specializing in providing automated solutions for system
monitoring. Your task is to create a "System Health Monitoring Bot" that tracks CPU and memory usage.

Objective:
Write a Python program that prompts the user to input their system's CPU usage (in %) and memory usage (in GB). The bot
will calculate and display whether the system is Underutilized, Optimal, or Overloaded, based on the following criteria:

CPU Usage:
•	Less than 40% = "Underutilized"
•	40% - 75% = "Optimal"
•	More than 75% = "Overloaded"
Memory Usage:
•	Less than 4GB = "Underutilized"
•	4GB - 8GB = "Optimal"
•	More than 8GB = "Overloaded"
"""

"""
Step One: Request that user inputs their CPU and memory usage.
Step Two: Calculate system status based on users input
Step Three: Print results
"""

# Start loop, This allows the user to start over if they wish to at the end
while True:
    # Print introduction text
    print("Hello! \n"
          "I am PHD Robot!\n"
          "Tech Comps state of the art System Health Monitoring Bot")

    # Ask users name to make program personal
    users_name = input("Please enter your name: ")
    #Print user Welcome, .title will capitalize the first character of users name
    print(f"Hello {users_name.title()}, Please enter the following information to determine the status of your system")

    # Ask the user for CPU usage, remove % symbol if user enters one, and ensure the value is between 0 and 100
    while True: #This starts a nested loop which allows user input to be validated and displays error message if required
        cpu_input = input("Please enter your system's CPU usage (%): ") #Request that user inputs their CPU usage

        # Check if the input ends with '%'
        if cpu_input.endswith('%'):
            # Remove '%' from the input by using strip to remove the last character of the string
            cpu_input = cpu_input[:-1].strip()

        # Check if the remaining input is a valid number
        if cpu_input.isdigit():
            cpu_usage = int(cpu_input) #convert user input to an integer, this will be used to determine system status

            # Ensure the CPU usage is between 0 and 100
            if 0 <= cpu_usage <= 100:
                break  # Exit the loop if valid input is entered
            else: #display error message to request number between 0-100
                print("Invalid input. Please enter a number between 0 and 100, optionally followed by '%'")
        else: #display error message to request whole number
            print("Invalid input. Please enter a whole number, optionally followed by '%'.")

    # Ask the user for memory usage, remove GB characters if user enters them
    while True: #This starts a nested loop which allows user input to be validated and displays error message if required
        memory_input = input("Please enter your system's memory usage to the nearest GB: ") #Request that user inputs their memory usage

        # Check if the input ends with 'GB' or 'gb'
        if memory_input.lower().endswith('gb'): #.lower converts users input to lowercase
            # Remove 'GB' from the input by using strip to remove last 2 characters from string
            memory_input = memory_input[:-2].strip()

        # Check if the remaining input is a whole number
        if memory_input.isdigit():
            memory_usage = int(memory_input) #convert user input to an integer, this will be used to determine system status
            break  # Exit the loop if valid input is entered
        else: #display error message to request whole number
            print("Invalid input. Please enter a whole number, optionally followed by 'GB'.")

    # Determine CPU status
    if cpu_usage < 40:
        cpu_status = "Underutilized" # If CPU usage is less than 40, status is Underutilized
    elif 40 <= cpu_usage <= 75:
        cpu_status = "Optimal" # If CPU usage is between 40 and 75, status is Optimal
    else:
        cpu_status = "Overloaded" # If CPU usage is above 75, status is Overloaded

    # Determine memory status
    if memory_usage < 4:
        memory_status = "Underutilized"  # If memory usage is less than 4, status is Underutilized
    elif 4 <= memory_usage <= 8:
        memory_status = "Optimal"  # If memory usage is between 4 and 8, status is Optimal
    else:
        memory_status = "Overloaded"  # If memory usage is above 8, status is Overloaded

    # Display results,
    print(f"{users_name.title()}'s CPU Usage is {cpu_usage}% which is {cpu_status}")
    print(f"{users_name.title()}'s Memory Usage is {memory_usage}GB which is {memory_status}")

    # Ask if the user wants to start over
    restart = input('\nThank you for using our service. Type "new" to start again, or any other key to exit: ')

    if restart.lower() != 'new': # != means 'not equal to', if restart input is not 'new', loop will break
        print('GoodBye')
        break  # Exit the loop if the user doesn't want to start over
