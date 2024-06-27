'''
Write a python program that takes few numbers as command line argument. Use a loop to display all elements.
Use another loop to display all elements in the even position. Use another loop to display all elements in the odd position.
'''

import sys

arguments = sys.argv[1:]

print("All elements:")
for element in arguments:
    print(element)

print("\nElements at even positions:")
for i in range(len(arguments)):
    if i % 2 == 0:
        print(arguments[i])

print("\nElements at odd positions:")
for i in range(len(arguments)):
    if i % 2 != 0:
        print(arguments[i])