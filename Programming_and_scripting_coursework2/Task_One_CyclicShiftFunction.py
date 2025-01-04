"""
You are required to design and implement a Python function that cyclically shifts a message m by
shift places rightwards.
For example, if
m is the string “This is a secret message” and
shift is 2
then the rightwards cyclic shift function applied to m and shift should return the string
“geThis is a secret messa”.
If shift is negative or greater or equal to the length of m then the function should return the original
message.
Develop pseudo-code for the function and then implement and test it. Include tests for the following:
1. m is a string
2. m is a list of numbers
3. m is a list of strings
4. m is a list of lists
(Functions that can process a range of datatypes are called polymorphic).
"""

"""
Step One: Define a function that can process a range of datatypes (polymorphic).
Step Two: Function should accept two inputs -
                                        m = the message to be shifted
                                        shift = the number of places to be shifted
Step Three: Validation. If shift is negative or greater or equal to the length of m then the function should return
the original message. Input should also be a string or list
Step Four: Calculate the effective shift 
Step Five: Perform the shift
Step Six: Print the new shifted message 
"""


def cyclic_shift(m, shift):
    # Check if the input is valid (string or list) by using isinstance function
    if not isinstance(m, (str, list)):
        raise TypeError("The message must be a string or a list.")

    # Check if the message is empty
    if len(m) == 0:
        return m  # If it's empty, return message as is.

    # Get the length of m
    mlength = len(m)

    # Handle cases where the shift is negative or too large
    if shift < 0 or shift >= mlength:
        return m  # Return the original message if shift is invalid.

    # Calculate the effective shift (to handle shifts larger than the message length)
    effective_shift = shift % mlength  # This makes sure the shift wraps around correctly.

    # Perform the cyclic shift - This creates a new version of m by combining two parts:
    # 1 - The part of the input that is to be shifted
    # 2 - The remainder of the input, starting from the beginning up to where the first part ends.
    shifted_m = m[-effective_shift:] + m[:-effective_shift]

    # Step 7: Return the shifted message
    return shifted_m

"""
Tests for the following:
1. m is a string
2. m is a list of numbers
3. m is a list of strings
4. m is a list of lists
"""

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