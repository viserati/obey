"""
-----------------------------------------
This is a multiline comment for the
rock, paper, scissors game. Not sure why
it shows up as green in the IDE?
-----------------------------------------
"""
#Import Module (Keep modules at the top of your page)
import random

winner = ''

#This varible calls the randint function.
random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'sissors'

user_choice = input('Choose Rock, Paper or Scissors: ')

if computer_choice == user_choice:
    winner ='Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

print('The' , winner, 'wins!')
