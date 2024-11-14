#List of numbers
Listnum= [25,33,72,81,49,50,101,23]
#initial greatest number is 0
greatest_num=0
#if initial greatest number is smaller than current number in list, change greatest number to current number
for num in Listnum:
    if greatest_num<num:
        greatest_num=num
#Print the greatest number
print(greatest_num)
