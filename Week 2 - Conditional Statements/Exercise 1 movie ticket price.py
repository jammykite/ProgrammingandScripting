while True:
 age = int(input('Please enter your age to check movie prices: '))

 if age>=18:
     print("Adult movie ticket costs £10")
 elif age>=12:
      print('Teen movie ticket costs £7')
 else:
    print('Child movie ticket costs £5')

