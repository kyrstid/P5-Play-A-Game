
# invite the user to play a friendly game
'Y' == 'y' == 'yes'
'N' == 'n' == 'no'

print('Hello, would you like to play a game of rock, papper, scissors with me?')
play_game = input('Select Y for yes or N for no: ')
if play_game == 'Y':
    print("Great, let's get started.")
else:
    if play_game == 'N':
        print("Too bad, maybe later?  Bye!")

 # get input from user and turn it into an int       
print("To make things easy, please choose from the following: ")
print("You can enter '1' for 'rock',  You can enter '2' for 'paper',  Or enter '3' for 'scissors - ")
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

print('You chose: ' + user_choice + '. ')
print('The computer chose: ' + comp_choice + '. ')

# determine the winner of the round
loop = 0
user_wins = 0
comp_wins = 0
ties = 0

for loop in play_game:
    if user_choice == comp_choice:
        winner = 'tie'
        ties += 1
        print('This round is a draw. Both players chose ' + user_choice + '.')
    if user_choice == 'rock':
        if comp_choice == 'paper':
                winner = 'Computer'
                comp_wins += 1
                print('You lose, paper covers rock.')
        if comp_choice == 'scissors':
            print('You win, rock smashes scissors.')
            winner = 'Gamer'
            user_wins += 1
    elif user_choice == 'paper':
                if comp_choice == 'rock':
                    winner = 'Gamer'
                    user_wins =+ 1
                print('You win, paper covers rock.')
                if comp_choice == 'scissors':
                    print('You lose, scissors cuts paper.')
                    winner = 'Computer'
                    comp_wins += 1
    else:
        if user_choice == 'scissors':
            if comp_choice == 'rock':
                winner = 'Computer'
                comp_wins += 1
                print('You lose, rock smashes scissors.')
        else: comp_choice = 'paper'
        winner = 'Gamer'
        user_wins += 1
        print('You win, scissors cuts paper.')
        loop += 1

user_tally = winner.count('Gamer')
comp_tally = winner.count('Computer')
tie_tally = winner.count('tie')

play_game = input('Select Y for yes or N for no: ')

while loop < 5:
    play_game == 'Y'
    if play_game == 'N':
                break
