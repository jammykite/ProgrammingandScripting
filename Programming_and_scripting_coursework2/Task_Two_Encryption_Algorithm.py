"""
A encryption algorithm with a secret key is described below. The algorithm applies cyclic shifts in two
different ways to a message. There are 9 stages:
1. Accept an encryption key containing 6 characters;
2. Accept a message m to be encrypted;
3. Pad out the message with additional “a” characters until its new length is a multiple of 8. The
message “abcdefghijklmnopqrstuv” is padded out to:
“abcdefghijklmnopqrstuvaa”
4. Split the new message into list of subsequences of 8 characters.
The message “abcdefghijklmnopqrstuvaa” splits into:
[“abcdefgh” , “ijklmnop” , “qrstuvaa”]
5. Calculate a shift shift1 from key as follows: convert the first two characters of key into their
ASCII integer values; add these two values together and find the remainder after division by
    8. The key “TheKey” has a shift1 value of (84+104) MOD 8 = 4.
6. Perform a right cyclic shift of size shift1 on each subsequence.
If shift1is 4, then the subsequences above becomes
“efghabcd” “mnopijkl” “uvaaqrst”
7. Calculate a shift shift2 from key as follows: convert the third and fourth characters of key into
their ASCII integer values; add these two values together and find the remainder after division
by 3.
Thee key “TheKey” has a shift2 value of (101+75) MOD 3 = 2.
8. Perform a cyclic shift of size shift2 on the list of subsequences (in part 6). If shift2 is 2 then
the list of subsequences becomes:
“mnopijkl” “uvaaqrst” “efghabcd”
9. Concatenate the subsequences together to form the encrypted message.
Implement the keyword encryption algorithm above.
"""

from Task_One_CyclicShiftFunction  import cyclic_shift  #import my function from previous task

def encryption_algorithm(key, m):
    #pad message until length is multiple of 8
    while len(m) % 8 != 0:
        m += 'a'

    #Split m into subsequences of 8 characters
    subsequences = [m[i:i+8] for i in range(0, len(m), 8)]

    #Calculate shift1 from the first two characters of the key
    shift1 = (ord(key[0]) + ord(key[1])) % 8

    #Perform a right cyclic shift of size shift1 on each subsequence
    shifted_subsequences = [cyclic_shift(subs, shift1) for subs in subsequences]

    #Calculate shift2 from the third and fourth characters of the key
    shift2 = (ord(key[2]) + ord(key[3])) % 3

    #Perform a cyclic shift of size shift2 on the list of subsequences
    shifted_subsequences2 = cyclic_shift(shifted_subsequences, shift2)

    #Concatenate the subsequences together to form the encrypted message
    encrypted_message = ''.join(shifted_subsequences2)

    return encrypted_message

# Example usage:
key = input("Please enter a 6-character encryption key: ")
m = input("Now enter a message to be encrypted: ")

# Encrypt the message
encrypt_message = encryption_algorithm(key, m)

# Output the encrypted message
print(f"The encrypted message is: {encrypt_message}")