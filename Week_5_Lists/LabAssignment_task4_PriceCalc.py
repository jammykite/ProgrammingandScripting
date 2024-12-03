"""
Write a program that:
1. Accepts product prices from the user.
2. Stores them in a list.
3. Calculates and prints the total cost.
"""

def get_prices():
    """Accept product prices from the user and store them in a list."""
    prices = []
    while True:
        price_input = input("Enter a product price (or type 'done' to finish): ").strip()
        if price_input.lower() == 'done':
            break
        try:
            price = float(price_input)
            if price >= 0:
                prices.append(price)
            else:
                print("Price cannot be negative. Please enter a valid price.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return prices

def calculate_total(prices):
    """Calculate and return the total cost of the prices."""
    return sum(prices)

def PriceCalc():
    """Main function to accept prices, calculate, and print the total cost."""
    print("Product Price Calculator")
    prices = get_prices()
    if prices:
        total_cost = calculate_total(prices)
        print(f"\nPrices entered: {prices}")
        print(f"Total cost: ${total_cost:.2f}")
    else:
        print("\nNo prices were entered.")

# Run the program
if __name__ == '__main__':
    PriceCalc()
