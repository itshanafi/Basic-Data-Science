'''
Write a Python program that:
Prompts the user to enter the principal amount, rate of interest, and time in years.
Calculates the simple interest. Prints the simple interest.
(Hint: The formula to calculate simple interest is: SI = (P * R * T) / 100)
'''

numPrincipal = float(input("Please enter your principal amount rate: "))
numRate = float(input("Please enter your interest rate: "))
numTime = float(input("Please enter your time in years: "))

P = numPrincipal
R = numRate
T = numTime

SI = (P * R * T) / 100

print("The interest is: ", SI)