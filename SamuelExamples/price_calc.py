"""
Write a program that:

Accepts product prices from the user.

Stores them in a list.

Calculates and prints the total cost.
"""
def price_calc():
    prices_list = []
    while True:
        current_price_item = input(f'Please enter a product price, when done enter "Q": ')
        if current_price_item.lower() == 'q':
            break
        try:
            prices_list.append(float(current_price_item))
        except ValueError:
            print(f'Invalid input, please enter a valid price!')
        if len(prices_list) == 0:
            print(f'No prices have been added to the price list!')
        else:
            total_price = sum(prices_list)
            print(f'The total price of all items in the list is: {total_price}')
    print(f'Total price of all items in the list is: {total_price}')

if __name__ == '__main__':
    price_calc()