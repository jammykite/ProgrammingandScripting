user_input = input("Please enter a word or phrase and I will count the vowels: ")
vowels = "aeiouAEIOU"
count = 0

for char in user_input:
    if char in vowels:
        count += 1


print(f"Number of vowels in {user_input} is:", count)
