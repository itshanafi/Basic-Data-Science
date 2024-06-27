'''
An investor decides to invest a total of RM30,000 in two different accounts.
The first account offers a 5% annual interest rate, while the second account offers a 7% annual interest rate.
If the total annual interest earned is RM1,800, how much money was invested in each account?
Another investor decides to invest a total of RM50,000 in two different accounts.
The first account offers a 3% annual interest rate, while the second account offers a 6% annual interest rate.
If the total annual interest earned is RM2,400, how much money was invested in each account?
Write a simple, generic Python program to assist in calculating the amount of money invested in each account
to achieve the desired total annual interest. The program must take all these numbers (30000, 5, 7, 1800) as input and
calculate the required amounts. Finally, print the result. Please note that the same program must work for the second problem
as well (50000, 3, 6, 2400).
'''

# For the first investor
total_investment = float(input("Enter the total amount of investment: "))
rate1 = float(input("Enter the annual interest rate for the first account: "))
rate2 = float(input("Enter the annual interest rate for the second account: "))
total_interest = float(input("Enter the total annual interest earned: "))

# Calculate the amount of money invested in each account
amount_invested1 = (total_interest - (total_investment * rate2 / 100)) / ((rate1 - rate2) / 100)
amount_invested2 = total_investment - amount_invested1

print(f"Amount invested in the first account: RM{amount_invested1:.2f}")
print(f"Amount invested in the second account: RM{amount_invested2:.2f}")

# For the second investor
total_investment = float(input("\nEnter the total amount of investment: "))
rate1 = float(input("Enter the annual interest rate for the first account: "))
rate2 = float(input("Enter the annual interest rate for the second account: "))
total_interest = float(input("Enter the total annual interest earned: "))

# Calculate the amount of money invested in each account
amount_invested1 = (total_interest - (total_investment * rate2 / 100)) / ((rate1 - rate2) / 100)
amount_invested2 = total_investment - amount_invested1

print(f"Amount invested in the first account: RM{amount_invested1:.2f}")
print(f"Amount invested in the second account: RM{amount_invested2:.2f}")
