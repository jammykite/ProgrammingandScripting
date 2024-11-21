"""write a program that creates a random list of length 500 containing integers from 125 to 2250"""

# Generate a random list of 500 integers between 125 and 2250
random_list = [random.randint(125, 2250) for _ in range(500)]

# Print the list (optional, as it might be too long to display fully)
print("Random list of 500 integers:")
print(random_list)
