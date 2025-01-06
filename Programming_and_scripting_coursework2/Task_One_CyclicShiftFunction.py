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
Pseudo-code
Step One: Define a function that can process a range of datatypes (polymorphic).
Step Two: Function should accept two inputs -
                                        m = the message to be shifted
                                        shift = the number of places to be shifted
Step Three: Validation. If shift is negative, greater or equal to the length of m then the function should return
the original message. Input should also be a string or list
Step Four: Calculate the effective shift, this is done using the % operator to find the remainder if shift value is
longer than message.
Step Five: Perform the shift
Step Six: Print the new shifted message 
"""

#def to create a new function
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

    # Calculate the effective shift (this helps to handle shifts larger than the message length)
    effective_shift = shift % mlength  # This makes sure the shift wraps around correctly.

    # Perform the cyclic shift - This creates a new version of m by slicing m according to the effective shift
    # and combining the two parts:
      # 1 - The part of the input that is to be shifted goes to the start
      # 2 - The remainder of the input goes to the end
    shifted_m = m[-effective_shift:] + m[:-effective_shift]

    # Step 7: Return the shifted message
    return shifted_m

