"""
Write a function that accepts a tuple of integers and returns the maximum and minimum
values.
"""


def find_max_min(values):
    if not values:  # Check if the tuple is empty
        raise ValueError("The input tuple cannot be empty.")

    return max(values), min(values)


# Example usage:
numbers = (3, 1, 9, 4, 7)
max_val, min_val = find_max_min(numbers)
print(f"Maximum value: {max_val}, Minimum value: {min_val}")
