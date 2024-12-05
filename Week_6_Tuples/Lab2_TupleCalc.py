"""
Write a function that accepts a tuple of integers and returns their sum and product.
"""

def calculate_sum_and_product(values):
    """
    Accepts a tuple of integers and returns their sum and product.

    Args:
        values (tuple): A tuple of integers.

    Returns:
        tuple: A tuple containing the sum and product of the integers.
    """
    if not values:  # Check if the tuple is empty
        raise ValueError("The input tuple cannot be empty.")

    total_sum = sum(values)
    total_product = 1
    for value in values:
        total_product *= value

    return total_sum, total_product


# Example usage:
numbers = (3, 4, 5)
sum_val, product_val = calculate_sum_and_product(numbers)
print(f"Sum: {sum_val}, Product: {product_val}")
