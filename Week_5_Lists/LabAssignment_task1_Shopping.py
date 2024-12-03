"""
Write a program to manage a shopping cart:
1. Allow the user to add items to the cart.
2. Remove items from the cart.
3. View all items in the cart.
"""


def display_menu():
    """Display the main menu for the shopping cart program."""
    print("\nMenu:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Exit")


def add_item(cart):
    """Add an item to the shopping cart."""
    item = input("Enter the name of the item to add: ").strip()
    if item:
        cart.append(item)
        print(f"'{item}' has been added to the cart.")
    else:
        print("Item name cannot be empty.")


def remove_item(cart):
    """Remove an item from the shopping cart."""
    if not cart:
        print("The cart is empty. Nothing to remove.")
        return

    item = input("Enter the name of the item to remove: ").strip()
    if item in cart:
        cart.remove(item)
        print(f"'{item}' has been removed from the cart.")
    else:
        print(f"'{item}' is not in the cart.")


def view_cart(cart):
    """View all items in the shopping cart."""
    if cart:
        print("\nItems in your cart:")
        for idx, item in enumerate(cart, start=1):
            print(f"{idx}. {item}")
    else:
        print("Your cart is empty.")


def shopping_cart_program():
    """Main function to run the shopping cart program."""
    cart = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            add_item(cart)
        elif choice == '2':
            remove_item(cart)
        elif choice == '3':
            view_cart(cart)
        elif choice == '4':
            print("Exiting the shopping cart program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Run the program
if __name__ == '__main__':
    shopping_cart_program()
