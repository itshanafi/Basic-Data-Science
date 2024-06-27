'''
Write a Python program that:
Prompts the user to enter the principal amount, rate of interest, time in years, and number of times interest is compounded per year.
Calculates the compound interest. Prints the compound interest.
(Hint: The formula to calculate compound interest is: A=P(1+R/100n)nt where A is the amount,
P is the principal amount, R is the annual interest rate, t is the time the money is invested for,
and n is the number of times interest is compounded per year)
'''

numPrincipal = float(input("Please enter your principal amount rate: "))
numRate = float(input("Please enter your interest rate: "))
numYears = float(input("Please enter your time in years: "))
numTime = float(input("Please enter your number of time interest: "))

P = numPrincipal
R = numRate
Y = numYears
T = numTime

A = P * (1 + (R / (100 * T))) * Y * T

print("The compound interest is: ", A)