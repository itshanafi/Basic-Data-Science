'''
Write a program that plays the game of Rock, Paper, Scissors with the user.
The user makes a choice, the program randomly chooses, and the winner is determined.
To generate random number use random module
'''

import random

print("ROCK VS PAPER VS SCISSOR GAME !")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice :"))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('Your choice is', choice_name.upper())

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is ", comp_choice_name.upper())
    print(choice_name, 'Vs', comp_choice_name)

    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"

    if (choice == 1 and comp_choice == 2):
        print('paper wins =>', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'RocK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins =>', end="")
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>', end="")
        result = 'Scissors'

    if result == 'DRAW':
        print("<== ITS A DRAW ==>")
    if result == choice_name:
        print("<== ITS YOUR WIN ==>")
    else:
        print("<== TOO BAD, COMPUTER WIN ==>")
    print("LET'S PLAY AGAIN? (Y/N)")

    ans = input().lower()
    if ans == 'n':
        break

print("THANK YOU FOR PLAYING!")