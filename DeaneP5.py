# KDeaneP5
# Programmer: Kyrsti Deane
# email: kdeane1@cnm.edu
# Purpose: PythonP5 - Rock, Paper, Scissors

import random
choices = ("rock", "paper", "scissors")
victor = {"rock":"scissors","paper":"rock","scissors":"paper"}
#tally = {"round":{"computer":"human"}}
tally = {}

#Get Input from User
print("\nWelcome, Let's play a game of Rock, Paper, Scissors!")
loop = 0
humanwins=0
compwins=0
ties=0

while True:
    humanchoice = input("Make your Choice of 'rock','paper',or 'scissors': ").strip().lower()
    compchoice = choices[random.randrange(3)]
    print ("Computer Chose:",compchoice)
    print ("Human Chose:",humanchoice)
    if victor[humanchoice] == compchoice:
        Winner = "Human"
        humanwins += 1
    elif victor[compchoice] == humanchoice:
        Winner = "Computer"
        compwins +=1
    else:
        Winner = "Tie"
        ties += 1
    print ("Winner of this round is {}!!".format(Winner))
    loop +=1
    tally[loop]={"winner": Winner,"Human Choice":humanchoice,"Computer Choice":compchoice,\
                 "Human wins":humanwins,"Comp wins":compwins,"Ties":ties}

    if loop == 5:
        break
print ("------")
print(tally)
for t in tally:
    print(t)
    print(tally[t]["winner"])
