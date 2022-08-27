
# KDeaneP5
# Programmer: Kyrsti Deane
# kdeane1@cnm.edu
# Purpose: write a program to play rock, paper, scissors with the user

# invite the user to play a friendly game
print('Hello, would you like to play a game of rock, papper, scissors with me?')
play_game = input('Select Y for yes or N for no: ' )

if play_game == 'Y':
    print("Great, let's get started.")
else:
    if play_game == 'N':
        print("Too bad, maybe later?  Bye!")

# loop games into 5 rounds
loop = 0
User Wins = 0
Comp Wins = 0
tie = 0

# get input from user and turn it into an int       
while play_game == 'Y':
    print("To make things easy, please choose from the following: ")
    print("You can enter '1' for 'rock',  You can enter '2' for 'paper',  Or enter '3' for 'scissors' - ")
user_entered = int(input("What is your choice: " ))
if user_entered > 3 or user_entered < 1:
    user_entered = (int(input("That's not an option. Please enter a valid choice: ")))
else:
    if user_entered == 1:
        user_choice = 'rock'
    elif user_entered == 2:
        user_choice = 'paper'
    else:
        user_choice = 'scissors'

# randomly generate the computer's choice

import random
computer_choice = random.randint(1, 3)

if computer_choice == 1:
    comp_choice = 'rock'
elif computer_choice == 2:
    comp_choice = 'paper'
else:
    comp_choice = 'scissors'
        break

# define the winner

def winner (user_choice, comp_choice):
    if user_choice == computer_choice:
        return "Tie"
    if user_choice == 'rock' and comp_choice == 'paper':
        return "Computer Wins"
        winner = 'Computer'
        comp_wins += 1
    if user_choice == 'paper' and comp_choice == 'scissors':
        return "Computer Wins"
        winner = 'Computer'
        comp_wins += 1
    if user_choice == 'scissors' and computer_choice == 'rock':
        return "Computer Wins"
        winner = 'Computer'
        comp_wins += 1
    else:
        return "User Wins"
        winner = 'Gamer'
        user_wins += 1

user_picks = user_choice
comp_picks = comp_choice

print('You chose: ' + user_choice + '. ')
print('The computer chose: ' + comp_choice + '. ')
result = winner(user_choice, comp_choice)
if result == 'Tie':
     print('This round is a draw. Both players chose ' + user_choice + '.')
elif result == 'Computer Wins':
    print('Sorry you lose.')
else:
    print('Great job, you won this round!')

print("Do you want to play again? (Y/N)")
answer = input().upper

answer = play_game
