import ast
import datetime
import time
import os

# Assuming customers_data and cars_data are defined and populated elsewhere in your program
customers_data = {}
cars_data = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_customer_and_car(customer_id):
    try:
        with open('Customer Detail.txt', 'r') as customer_file:
            customers_data = ast.literal_eval(customer_file.read())
        
        with open('Car Detail.txt', 'r') as car_file:
            cars_data = ast.literal_eval(car_file.read())
        
        if customer_id in customers_data:
            customer = customers_data[customer_id]
            car_id = customer['CarID']
            if car_id in cars_data:
                car = cars_data[car_id]
                return customer, car
            else:
                print(f"Car details not found for CarID: {car_id}")
                return None, None
        else:
            print(f"Customer ID '{customer_id}' not found.")
            return None, None
    
    except FileNotFoundError:
        print("Error: One or both data files not found.")
        return None, None
    except ValueError:
        print("Error: Failed to parse data from one or both files.")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None, None

def calculate_payment(customer, car):
    try:
        start_date = datetime.datetime.strptime(customer['Startdate'], "%Y-%m-%d")
        end_date = datetime.datetime.strptime(customer['Enddate'], "%Y-%m-%d")
        rental_days = (end_date - start_date).days
        
        price_per_day = float(car['Price/day'].replace("RM", ""))
        total_payment = (rental_days * price_per_day) / 2
        
        return total_payment
    
    except ValueError:
        print("Error: Failed to calculate payment.")
        return None

def make_payment_credit_card(customer_id):
    customer, car = display_customer_and_car(customer_id)
    cardInfo()
    
    if customer and car:
        total_payment = calculate_payment(customer, car)
        if total_payment is not None:
            current_balance = float(customer['Balance'].replace("RM", ""))
            
            if current_balance >= total_payment:
                new_balance = current_balance - total_payment
                customers_data[customer_id]['Balance'] = f"RM{new_balance:.2f}"
                print(f"Total Payment: RM {total_payment:.2f}")
                print(f"Remaining Balance: RM {new_balance:.2f}")
                card_info = cardInfo()
                if card_info:
                    display_invoice(customer_id)
                    return True
            else:
                print("Insufficient balance.")
    
    return False

def cardInfo():
    print("\nEnter the card number: ")
    while True:
        try:
            cardNumber = input().replace(" ", "").strip()
            if not cardNumber.isdigit() or len(cardNumber) != 16:
                print("\nCard number must be 16 digits")
                continue
            
            # Determine card type based on card number prefix
            first_digit = cardNumber[0]
            if first_digit == '3':
                if cardNumber[1] == '4' or cardNumber[1] == '7':
                    card_type = "American Express"
                else:
                    card_type = "Unknown"
            elif first_digit == '4':
                card_type = "Visa"
            elif first_digit == '5':
                card_type = "Mastercard"
            elif first_digit == '6':
                card_type = "Discover"
            else:
                card_type = "Unknown"

            break
        except ValueError:
            print("\nInvalid card number")
    
    print("\nEnter the card holder name: ")
    cardHolderName = input().strip()

    print("\nEnter the expiry date (MMYY): ")
    while True:
        try:
            expiryDate = input().strip()
            if len(expiryDate) != 4 or not expiryDate.isdigit():
                print("\nExpiry date must be 4 digits in the format MMYY")
                continue
            
            month = int(expiryDate[:2])
            year = int(expiryDate[2:])
            
            if month < 1 or month > 12:
                print("\nInvalid month in expiry date")
                continue
            
            current_year = int(str(datetime.datetime.now().year)[2:])
            if year < current_year or (year == current_year and month < datetime.datetime.now().month):
                print("\nInvalid expiry date")
                continue
            
            break
        except ValueError:
            print("\nInvalid expiry date")

    print("\nEnter the CVV / CVC: ")
    while True:
        try:
            cvv = int(input().strip())
            if len(str(cvv)) != 3 or cvv < 100:
                print("\nCVV must be 3 digits")
                continue
            break
        except ValueError:
            print("\nInvalid CVV")
    

    print("\nProcessing... Please wait...")
    time.sleep(2)  # Simulating processing time

    clear_screen()  # Clear the screen before displaying success message

    print(f"Card Type: {card_type}")
    print(f"Card Number: {'*' * 12}{cardNumber[-4:]}")
    print(f"Card Holder: {cardHolderName}")
    print(f"Expiry Date: {expiryDate[:2]}/{expiryDate[2:]}")
    
    # Example: Return or store card information
    return cardNumber, cardHolderName, expiryDate, cvv, card_type

def make_payment_eWallet(customer_id, wallet_name):
    customer, car = display_customer_and_car(customer_id)
    
    if customer and car:
        total_payment = calculate_payment(customer, car)
        if total_payment is not None:
            if float(customer['Balance'].replace("RM", "")) >= total_payment:
                new_balance = float(customer['Balance'].replace("RM", "")) - total_payment
                customers_data[customer_id]['Balance'] = f"RM{new_balance:.2f}"
                print(f"Total Payment: RM {total_payment:.2f}")
                print(f"Remaining Balance: RM {new_balance:.2f}")
                confirmPayment(wallet_name)
                display_invoice(customer_id)
                return True
            else:
                print("Insufficient balance.")

    return False

def choose_eWallet(customer_id):
    print("\nPlease choose the type of eWallet: ")
    print("1. GrabPay")
    print("2. TnG")
    print("3. BigPay")
    print("4. ShopeePay")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            make_payment_eWallet(customer_id, "GrabPay")
            break
        elif choice == "2":
            make_payment_eWallet(customer_id, "TnG")
            break
        elif choice == "3":
            make_payment_eWallet(customer_id, "BigPay")
            break
        elif choice == "4":
            make_payment_eWallet(customer_id, "ShopeePay")
            break
        elif choice == "5":
            print("\nExit.....")
            break
        else:
            print("Invalid choice")

def bankTransfer(customer_id):
    print("\nPlease choose the type of bank transfer: ")
    print("1. MayBank")
    print("2. Public Bank")
    print("3. Bank Islam")
    print("4. Exit")
    
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            make_payment_bank_transfer(customer_id, "MayBank")
            break
        elif choice == "2":
            make_payment_bank_transfer(customer_id, "Public Bank")
            break
        elif choice == "3":
            make_payment_bank_transfer(customer_id, "Bank Islam")
            break
        elif choice == "4":
            print("\nExit.....")
            break
        else:
            print("Invalid choice")

def make_payment_bank_transfer(customer_id, bank_name):
    customer, car = display_customer_and_car(customer_id)
    bankInfo()
    
    if customer and car:
        total_payment = calculate_payment(customer, car)
        if total_payment is not None:
            # Simulate bank transfer process
            username, password = bankInfo(bank_name)
            if username and password:  # Assume validation or authentication success
                new_balance = float(customer['Balance'].replace("RM", "")) - total_payment
                customers_data[customer_id]['Balance'] = f"RM{new_balance:.2f}"
                print(f"Total Payment: RM {total_payment:.2f}")
                print(f"Remaining Balance: RM {new_balance:.2f}")
                display_invoice(customer_id)
                return True
            else:
                print("Bank authentication failed.")
    
    return False

def bankInfo(bank_name):
    print(f"\nSelected: {bank_name}")
    print("\nPlease Enter Your Username: ")
    username = input().strip()
    print("\nPlease Enter Your Password: ")
    password = input().strip()  # Handle password securely if storing is required

    # Simulate payment process or confirmation step
    time.sleep(5)  # Simulating processing time
    clear_screen()  # Clear the screen before displaying success message
    print("Payment confirmed!")
    
    return username, password

def confirmPayment(wallet_name):
    print(f"\nYou have selected {wallet_name} for payment.")
    print("Please confirm your payment details.")
    # Simulate payment process or confirmation step
    time.sleep(5)  # Simulating processing time
    clear_screen()  # Clear the screen before displaying success message
    print("Payment confirmed!")

def display_invoice(customer_id):
    customer, car = display_customer_and_car(customer_id)
    if customer and car:
        print("\n===== Invoice =====")
        print(f"Customer ID: {customer_id}")
        print(f"Customer Name: {customer['Name']}")
        print(f"Car ID: {customer['CarID']}")
        print(f"Car Model: {car['Model']}")
        print(f"Start Date: {customer['Startdate']}")
        print(f"End Date: {customer['Enddate']}")
        print(f"Total Payment: {calculate_payment(customer, car):.2f} RM")
        print("===================")

def main():
    print("\nPlease select a payment method: ")
    print("1. Credit Card")
    print("2. eWallet")
    print("3. Bank Transfer")
    print("4. Exit")
    
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nSelected: Credit Card")
            print("\nEnter your Customer ID:")
            customer_id = input().strip()
            make_payment_credit_card(customer_id)
            break
        elif choice == "2":
            print("\nSelected: eWallet")
            print("\nEnter your Customer ID:")
            customer_id = input().strip()
            choose_eWallet(customer_id)
            break
        elif choice == "3":
            print("\nSelected: Bank Transfer")
            print("\nEnter your Customer ID:")
            customer_id = input().strip()
            bankTransfer(customer_id)
            break
        elif choice == "4":
            print("\nExit.....")
            break
        else:
            print("\nInvalid choice")

if __name__ == "__main__":
    main()
