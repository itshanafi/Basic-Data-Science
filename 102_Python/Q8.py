'''
Write a program that simulates an ATM withdrawal. The user enters the withdrawal amount and the program checks
if the amount is a multiple of 10. If it is, the program prints the number of each denomination (50, 20, 10) required
to dispense the amount. If not, it prints an error message. For example if the amount is 233 then it must
print "4 50 dollar bills, 1 20 dollar bills, 1 10 dollar bills, 3 1 dollar bills
'''

amount = int(input("Plase enter the withdrawal amount: "))

if(amount % 10 != 0):
    print("Error: Amount must be a multiple of 10.")
else:
    fifty_dollars = amount // 50
    remaining = amount % 50
    twenty_dollars = remaining // 20
    remaining = remaining % 20
    ten_dollars = remaining // 10
    remaining = remaining % 10

    print(f"{fifty_dollars} 50 dollar bills, {twenty_dollars} 20 dollar bills, {ten_dollars} 10 dollar bills")