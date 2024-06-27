'''
Write a program that randomly generates a number between 1 and 100. The user has to guess the number.
After each guess, the program tells the user whether the guess is too high, too low, or correct.
The game continues until the user guesses the correct number.
To generate random number use random module
'''

import random

number_to_guess = random.randint(1, 100)
guess = 0

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")

print("YOU GUESS IT RIGHT !")