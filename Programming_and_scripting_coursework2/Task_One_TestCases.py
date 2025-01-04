"""
Tests for the following:
1. m is a string
2. m is a list of numbers
3. m is a list of strings
4. m is a list of lists
"""

from Task_One_CyclicShiftFunction import cyclic_shift  #import my function

# Test cases
# Case 1: String
m1 = "This is a test"
shift1 = 2
print(cyclic_shift(m1, shift1))  # Expected output: "stThis is a te"

# Case 2: List of numbers
m2 = [1, 2, 3, 4, 5]
shift2 = 2
print(cyclic_shift(m2, shift2))  # Expected output: [4, 5, 1, 2, 3]

# Case 3: List of strings
m3 = ["This", "is", "a", "list", "of", "strings"]
shift3 = 3
print(cyclic_shift(m3, shift3))  # Expected output: ['list', 'of', 'strings', 'This', 'is', 'a']

# Case 4: List of lists
m4 = [[1, 2], [3, 4], [5, 6], [7, 8]]
shift4 = 1
print(cyclic_shift(m4, shift4))  # Expected output: [[7, 8], [1, 2], [3, 4], [5, 6]]

# Case 5: Negative shift or large shift
m5 = "Hello"
shift5 = -1
print(cyclic_shift(m5, shift5))  # Expected output: "Hello"


"""How can you unencrypt a cyclically shifted text (HINT: use the same function)?"""

"""To unencrypt a shifted text you first need to figure out the shift value. This can be 
done by using a FOR loop to iterate over all possible shift values. The number of possible shifts
is limited by the length of the input. Once all possible shifts are listed, human judgement or
automated checks such as matching against dictionaries can be used to identify the original message"""

# Example Usage
encrypted_message = "geThis is a secret messa"

# Iterate over all possible shift values
mlength = len(encrypted_message)
for shift in range(1, mlength):
    # Calculate the reverse shift (right shift by mlength - shift)
    reverse_shift = mlength - shift
    # Decrypt using the reverse shift
    decrypted_message = cyclic_shift(encrypted_message, reverse_shift)
    print(f"Shift {shift}: {decrypted_message}")