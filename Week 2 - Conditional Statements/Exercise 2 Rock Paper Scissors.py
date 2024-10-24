#while true creates a loop
while True:
    #import random to allow CPU choice to be randomised
 import random
    #print game title
 print ('Rock! Paper! Scissors!')
 print('New Game')
    #define player choice, CPU choice and moves
 player_choice = input('Enter your choice: ').title()
 moves = ('Rock', 'Paper', 'Scissors')
 computer_choice = random.choice(moves)
 print("CPU chose:", computer_choice)

#define game outcomes and print
 if computer_choice == player_choice:
     print("It's a tie!")
 elif (player_choice == 'rock' and computer_choice == 'scissors'):
     print("Rock beats Scissors! You win!")
 elif (player_choice == 'scissors' and computer_choice == 'paper'):
     print("Scissors beats Paper! You win!")
 elif (player_choice == 'paper' and computer_choice == 'rock'):
     print("Paper beats Rock! You win!")
 elif (computer_choice == 'rock' and player_choice == 'scissors'):
     print("Rock beats Scissors! CPU wins!")
 elif (computer_choice == 'scissors' and player_choice == 'paper'):
     print("Scissors beats Paper! CPU wins!")
 elif (computer_choice == 'paper' and player_choice == 'rock'):
     print("Paper beats Rock! CPU wins!")
 else:
     print("Invalid choice! CPU Wins by default. Please choose rock, paper, or scissors.")

