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
Step Four: Perform the shift
Step Five: Print the new shifted message 
"""