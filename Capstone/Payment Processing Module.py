# Create a module of payment processing system for car rental
# The module should have the following functions:
# 1. Calculate the total cost of the rental based on the number of days and the cost
#    of the car per day. The cost of the car per day should be a parameter of
#    the function.

import datetime
def cardInfo():
    print("Enter the card number: ")
    while True:
        try:
            cardNumber = input().replace(" ", "").strip() # 4693 0902 5971 4414
            if not cardNumber.isdigit() or len(cardNumber) != 16:
                print("Card number must be 16 digits")
                continue  # Ask for input again
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid card number")
    
    print("Enter the card holder name: ")
    cardHolderName = input().strip()

    print("Enter the expiry date (MMYY): ")
    while True:
        try:
            expiryDate = input().strip()
            if len(expiryDate) != 4 or not expiryDate.isdigit():
                print("Expiry date must be 4 digits in the format MMYY")
                continue  # Ask for input again
            
            # Convert to integers for validation
            month = int(expiryDate[:2])
            year = int(expiryDate[2:])
            
            if month < 1 or month > 12:
                print("Invalid month in expiry date")
                continue  # Ask for input again
            
            current_year = int(str(datetime.datetime.now().year)[2:])
            if year < current_year or (year == current_year and month < datetime.datetime.now().month):
                print("Invalid expiry date")
                continue  # Ask for input again
            
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid expiry date")
    
    print("Enter the CVV / CVC: ")
    while True:
        try:
            cvv = int(input().strip())
            if len(str(cvv)) != 3 or cvv < 100:
                print("CVV must be 3 digits")
                continue  # Ask for input again
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid CVV")
    
    return cardNumber, cardHolderName, expiryDate, cvv

def eWallet():
    print("\nPlease choose the type of eWallet: ")
    print("1. GrabPay")
    print("2. TnG")
    print("3. BigPay")
    print("4. ShopeePay")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            print("GrabPay")
            break
        elif choice == "2":
            print("TnG")
            break
        elif choice == "3":
            print("BigPay")
            break
        elif choice == "4":
            print("ShopeePay")
            break
        elif choice == "5":
            print("\nExit.....")
            break
        else:
            print("Invalid choice")


def bankTransfer():
    print("\nPlease choose the type of bank transfer: ")
    print("1. MayBank")
    print("2. Public Bank")
    print("3. Bank Islam")
    print("4. Exit")
    
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            bankInfo()
            break
        elif choice == "2":
            bankInfo()
            break
        elif choice == "3":
            bankInfo()
            break
        elif choice == "4":
            print("\nExit.....")
            break
        else:
            print("Invalid choice")

def bankInfo():
    print("\nPlease Enter Your Username: ")
    username = input()
    print("\nPlease Enter Your Password: ")
    password = input().__hash__()
    print(password)
    return username, password

bankTransfer()








# Example usage:
# card_number, card_holder_name, expiry_date, cvv = cardInfo()
# print("Card Number:", card_number)
# print("Card Holder Name:", card_holder_name)
# print("Expiry Date:", expiry_date)
# print("CVV:", cvv)























# def Cash():
#     print("Please call..... and make a payment")


    
