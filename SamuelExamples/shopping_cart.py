"""
Write a program to manage a shopping cart:

Allow the user to add items to the cart.

Remove items from the cart.

View all items in the cart.

"""
# Define a function to add items to the cart

def shopping_cart_list():
    """
    This function allows the user to add items to the cart.
    By following instructions.
    1.  Add item to the cart
    2. Remove item from the cart
    3. View all items in the cart
    4. Exit the program
    Returns:

    """
    print(f'Welcome to your Shopping Cart!')
    print(f'What would you like to do today?')
    cart = []
    while True:
        print(f'1. Add item to the cart')
        print(f'2. Remove item from the cart')
        print(f'3. View all items in the cart')
        print(f'4. Exit the program')
        choice = int(input(f'Please pick from option 1 - 4: '))
        if choice == 1:
            item = input(f'Please enter the item you would like to add to the cart: ')
            print(f'{item} has been added to the cart.')
            cart.append(item)
        elif choice == 2:
            item = input(f'Please enter the item you would like to remove from the cart: ')
            if item in cart:
                cart.remove(item)
                print(f'{item} has been removed from the cart.')
            else:
                print(f'Sorry the item you want to remove is not in the cart!')
        elif choice == 3:
            print(f'The following items are in the cart: ')
            if len(cart) == 0:
                print(f'Sorry, your cart is empty, consider adding items to the cart!')
            else:
                for idx, ct in enumerate(cart):
                    print(f'Item {idx + 1} in cart is {ct}')
        elif choice == 4:
            print(f'Thank you for using the shopping cart!')
            print(f'Exiting ....')
            break
        else:
            print(f'Sorry, invalid choice! Please pick from option 1 - 4: ')

"""Write a program that: 

Accepts grades from the user (use a loop). 

Stores the grades in a list. 

Calculates and prints the average grade. """

def average_of_grades():
    """
    This function will accept grades from the user and calculate the average grade.
    This users have the following options:
    1. Add grades to the list
    2. Remove grades from the list
    3. View all grades in the list
    4. Calculate the average grade
    5. Exit the program
    Returns: float of the class average grade.

    """
    print(f'Welcome to your Class Average Calculation')
    print(f'What would you like to do today?')
    grades_list = []
    while True:
        print(f'1. Add grades to the list')
        print(f'2. Remove grades from the list')
        print(f'3. View all grades in the list')
        print(f'4. Calculate Class average grade')
        print(f'5. Exit the program')
        choice = int(input(f'Please pick from option 1 - 5: '))
        if choice == 1:
            item = float(input(f'Please enter the grade you would like to add to the list: '))
            print(f'{item} has been added to the cart.')
            grades_list.append(item)
        elif choice == 2:
            item = float(input(f'Please enter the grade you would like to remove from the list: '))
            if item in grades_list:
                grades_list.remove(item)
                print(f'{item} has been removed from the grades list.')
            else:
                print(f'Sorry the grades you want to remove is not in the grades list!')
        elif choice == 3:
            print(f'The following items are in the cart: ')
            if len(grades_list) == 0:
                print(f'Sorry, your grades list is empty, consider adding grades to the list!')
            else:
                for idx, ct in enumerate(grades_list):
                    print(f'Grades {idx + 1} in grades list is {ct}')
        elif choice == 4:
            if len(grades_list) == 0:
                print(f'Sorry, your grades list is empty, consider adding grades to the list!')
            else:
                sum_grades = sum(grades_list)
                num_grades = len(grades_list)
                average_grade = sum_grades / num_grades
                print(f'The average grade of the class is: {average_grade:.2f}')

        elif choice == 5:
            print(f'Thank you for using the Calculator for Grades List!')
            print(f'Exiting ....')
            break
        else:
            print(f'Sorry, invalid choice! Please pick from option 1 - 5: ')

if __name__ == '__main__':
    # shopping_cart_list()
    average_of_grades()

