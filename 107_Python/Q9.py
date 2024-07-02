# Write a Python class BankAccount with attributes like accountNumber, openingBalance,
# currentBalance dateOfOpening and customerName. Add methods like deposit, withdraw, and checkBalance

class BankAccount:
    def __init__(self, accountNumber, openingBalance, currentBalance, dateOfOpening, customerName):
        self.accountNumber = accountNumber
        self.openingBalance = openingBalance
        self.currentBalance = currentBalance
        self.dateOfOpening = dateOfOpening
        self.customerName = customerName

    def deposit(self, amount):
        self.currentBalance += amount
        print(f"Deposited {amount}. Current balance: {self.currentBalance}")

    def withdraw(self, amount):
        if amount <= self.currentBalance:
            self.currentBalance -= amount
            print(f"Withdrew {amount}. Current balance: {self.currentBalance}")
        else:
            print("Insufficient funds.")

    def checkBalance(self):
        print(f"Current Balance: {self.currentBalance}")

def main():
    accountNumber = int(input("Enter account number: "))
    openingBalance = float(input("Enter opening balance: "))
    currentBalance = float(input("Enter current balance: "))
    dateOfOpening = input("Enter date of opening: ")
    customerName = input("Enter customer name: ")

    # Create an instance of BankAccount
    bankAccount = BankAccount(accountNumber, openingBalance, currentBalance, dateOfOpening, customerName)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            bankAccount.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            bankAccount.withdraw(amount)
        elif choice == '3':
            bankAccount.checkBalance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

