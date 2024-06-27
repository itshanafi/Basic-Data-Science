'''
Write a Python program that:
Prompts the user to enter two numbers. Swaps the values of the two variables.
Prints the values before and after swapping.
'''

numFirst = float(input("Please enter your first number: "))
numSecond = float(input("Please enter your second number: "))

x = numFirst
y = numSecond

print(f"The before swaps value: first number {x} and second number {y}")

x , y = y , x

print(f"The after swaps number: first number {x} and second number {y}")