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
random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = "Rock"
elif random_choice == 1:
    computer_choice = "Paper"
else:
    computer_choice = "Sissors"

user_choice = input('Choose Rock, Paper or Scissors: ')

if computer_choice == user_choice
    winner ='Tie'
