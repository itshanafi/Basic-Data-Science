# A six sided die was rolled many times and the results of the rolls were saved to a numpy array called dice_rolls.
# How many times was a roll greater than 2 rolled? In other words, how many of the integers in the dice_rolls array are greater than 2?
# Can you write a Python program to solve the above problem?
# Refer Sample Input and Output for formatting specifications.
# All text in bold corresponds to input and the rest corresponds to output.
# Sample Input and Output :
# Enter the number of dice rolls
# 3
# Enter the value of each dice roll
# 1
# 2
# 3
# Dice rolls greater than 2
# 1

import numpy as np

def main():
    num_rolls = int(input("Enter the number of dice rolls\n"))
    print("Enter the value of each dice roll")
    dice_rolls = np.array([int(input()) for _ in range(num_rolls)])
    greater_than_2 = np.sum(dice_rolls > 2)
    print(f"Dice rolls greater than 2\n{greater_than_2}")

if __name__ == "__main__":
    main()