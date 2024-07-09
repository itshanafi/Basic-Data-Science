import ast
import datetime
import time
import os

class RentalService:
    def __init__(self):
        self.customers_data = {}
        self.cars_data = {}

    def read_data(self, file_name):
        try:
            with open(file_name, 'r') as file:
                return ast.literal_eval(file.read())
        except FileNotFoundError:
            print(f"Error: {file_name} not found.")
            return None
        except ValueError:
            print(f"Error: Failed to parse data from {file_name}.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return None

    def read_customer_and_car_data(self):
        self.customers_data = self.read_data('Customer Detail.txt')
        self.cars_data = self.read_data('Car Detail.txt')
        
        if self.customers_data is None or self.cars_data is None:
            return False
        return True

    def display_customer_and_car(self, customer_id):
        try:
            customer = self.customers_data.get(customer_id)
            if not customer:
                print(f"Customer ID '{customer_id}' not found.")
                return None, None

            car_id = customer.get('CarID')
            car = self.cars_data.get(car_id)
            if not car:
                print(f"Car details not found for CarID: {car_id}")
                return customer, None

            return customer, car
        except Exception as e:
            print(f"An error occurred while displaying customer and car data: {str(e)}")
            return None, None

    def calculate_deposit(self, customer, car):
        try:
            start_date = datetime.datetime.strptime(customer['Startdate'], "%Y-%m-%d")
            end_date = datetime.datetime.strptime(customer['Enddate'], "%Y-%m-%d")
            rental_days = (end_date - start_date).days + 1
            
            price_per_day = float(car['Price/day'].replace("RM", ""))
            total_deposit = (rental_days * price_per_day) // 3
            
            return total_deposit
        except Exception as e:
            print(f"An error occurred during deposit calculation: {str(e)}")
            return None

    def calculate_payment(self, customer, car):
        try:
            start_date = datetime.datetime.strptime(customer['Startdate'], "%Y-%m-%d")
            end_date = datetime.datetime.strptime(customer['Enddate'], "%Y-%m-%d")
            rental_days = (end_date - start_date).days + 1
            
            price_per_day = float(car['Price/day'].replace("RM", ""))
            total_payment = rental_days * price_per_day
            
            return total_payment
        except Exception as e:
            print(f"An error occurred during payment calculation: {str(e)}")
            return None

    def get_customer_id(self):
        try:
            while True:
                customer_id = input("Enter Customer ID: ").strip()
                if customer_id in self.customers_data:
                    return customer_id
                print(f"Customer ID '{customer_id}' not found. Please enter a valid ID.")
        except Exception as e:
            print(f"An unexpected error occurred during customer ID retrieval: {str(e)}")
            return None

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def process_credit_card_payment(self, customer_id):
        try:
            self.display_invoice(customer_id, "Credit Card")
            while True:
                card_number = input("\nEnter the card number (16 digits): ").replace(" ", "").strip()
                if len(card_number) != 16 or not card_number.isdigit():
                    print("\nInvalid card number format. Please enter a valid 16-digit number.")
                    continue

                card_holder_name = input("\nEnter the card holder name: ").strip()

                expiry_date = input("\nEnter the expiry date (MMYY): ").replace('/', '').strip()
                if len(expiry_date) != 4 or not expiry_date.isdigit():
                    print("\nInvalid expiry date format. Please enter MMYY.")
                    continue

                month = int(expiry_date[:2])
                year = int(expiry_date[2:])
                current_year = datetime.datetime.now().year % 100

                if year < current_year or (year == current_year and month < datetime.datetime.now().month):
                    print("\nInvalid expiry date. Please enter a future date.")
                    continue

                cvv = input("\nEnter the CVV / CVC (3 digits): ").strip()
                if len(cvv) != 3 or not cvv.isdigit():
                    print("\nInvalid CVV format. Please enter a valid 3-digit number.")
                    continue

                print("\nProcessing... Please wait...")
                time.sleep(2)  # Simulating processing time
                self.clear_screen()  # Clear the screen before displaying success message

                print("\nYour payment has been successful!")
                print(f"Card Number: {'*' * 12}{card_number[-4:]}")
                print(f"Card Holder: {card_holder_name}")
                print(f"Expiry Date: {expiry_date[:2]}/{expiry_date[2:]}")

                self.confirm_payment("Credit Card", customer_id)
                break
        except Exception as e:
            print(f"An unexpected error occurred during credit card payment: {str(e)}")

    def process_e_wallet_payment(self, customer_id):
        try:
            self.display_invoice(customer_id, "eWallet")
            print(f"\nSelected: eWallet")
            print(f"Customer ID entered: {customer_id}")

            customer = self.customers_data.get(customer_id)
            if not customer:
                print(f"Customer with ID '{customer_id}' not found in customers data. Please try again.")
                return

            car_id = customer.get('CarID')
            car = self.cars_data.get(car_id)
            if not car:
                print(f"Car with ID '{car_id}' not found in cars data. Please try again.")
                return

            total_deposit = self.calculate_deposit(customer, car)
            if total_deposit is None:
                return

            current_balance = float(customer['Balance'].replace("RM", ""))
            if current_balance >= total_deposit:
                new_balance = current_balance - total_deposit
                self.customers_data[customer_id]['Balance'] = f"RM{new_balance:.2f}"
                print(f"Total Payment: RM {total_deposit:.2f}")
                print(f"Remaining Balance: RM {new_balance:.2f}")
                self.confirm_payment("eWallet", customer_id)
            else:
                print("Insufficient balance. Please choose another payment method.")
        except Exception as e:
            print(f"An unexpected error occurred during eWallet payment: {str(e)}")

    def process_bank_info(self, bank_name, customer_id):
        try:
            self.display_invoice(customer_id, "Bank Transfer - " + bank_name)
            print(f"\nSelected: {bank_name}")
            username = input("\nPlease Enter Your Username: ").strip()
            password = input("\nPlease Enter Your Password: ").strip()  # Handle password securely if storing is required

            print("\nProcessing... Please wait...")
            time.sleep(3)  # Simulating processing time
            self.clear_screen()  # Clear the screen before displaying success message
            print("Payment confirmed!")

            self.confirm_payment("Bank Transfer - " + bank_name, customer_id)
        except Exception as e:
            print(f"An unexpected error occurred during bank information input: {str(e)}")

    def confirm_payment(self, wallet_name, customer_id):
        try:
            print(f"\nYou have selected {wallet_name} for payment.")
            print("Please confirm your payment details.")
            time.sleep(5)  # Simulating processing time
            self.clear_screen()  # Clear the screen before displaying success message
            print("Payment confirmed!")
            self.display_invoice(customer_id, wallet_name)
        except Exception as e:
            print(f"An unexpected error occurred during payment confirmation: {str(e)}")

    def cash_payment(self, customer_id):
        try:
            # Display the invoice for the customer
            self.display_invoice(customer_id, "Cash")

            customer, _ = self.display_customer_and_car(customer_id)
            if customer:
                print(f"Please pay at the counter before {customer['Startdate']}")
            else:
                print("Failed to find customer details. Please try again.")
                self.main()
                self.clear_screen()
        except Exception as e:
            print(f"An unexpected error occurred during cash payment: {str(e)}")

    def display_invoice(self, customer_id, payment_method):
        try:
            customer, car = self.display_customer_and_car(customer_id)
            if not customer or not car:
                print("Failed to generate invoice. Customer or car details not found.")
                return

            total_payment = self.calculate_payment(customer, car)
            total_deposit = self.calculate_deposit(customer, car)

            start_date = datetime.datetime.strptime(customer['Startdate'], "%Y-%m-%d")
            end_date = datetime.datetime.strptime(customer['Enddate'], "%Y-%m-%d")
            rental_days = (end_date - start_date).days + 1

            if total_payment is not None and total_deposit is not None:
                self.clear_screen()
                print("=" * 100)
                print(f"{'':^100}")
                print(f"{'RENTAL INVOICE':^100}")
                print("=" * 100)
                print(f"{'CUSTOMER DETAILS':^100}")
                print("=" * 100)
                print(f"{'Name':<20}: {customer.get('Name', 'N/A')}")
                print(f"{'Address':<20}: {customer.get('Address', 'N/A')}")
                print(f"{'Phone':<20}: {customer.get('Phone', 'N/A')}")
                print(f"{'IC No':<20}: {customer.get('IC No', 'N/A')}")
                print(f"{'Startdate':<20}: {customer.get('Startdate', 'N/A')}")
                print(f"{'Enddate':<20}: {customer.get('Enddate', 'N/A')}")
                print("=" * 100)
                print(f"{'CAR DETAILS':^100}")
                print("=" * 100)
                print(f"{'Brand':<20}: {car.get('Brand', 'N/A')}")
                print(f"{'Type':<20}: {car.get('Type', 'N/A')}")
                print(f"{'Plate Number':<20}: {car.get('Plate Num', 'N/A')}")
                print(f"{'Price/day':<20}: {car.get('Price/day', 'N/A')}")
                print(f"{'Days rent':<20}: {rental_days}")
                print("=" * 100)

                cash_tick = 'X' if payment_method == 'Cash' else ' '
                credit_card_tick = 'X' if payment_method == 'Credit Card' else ' '
                ewallet_tick = 'X' if payment_method == 'eWallet' else ' '
                bank_transfer_tick = 'X' if payment_method.startswith('Bank Transfer') else ' '

                print(f"{'Payment Method:':<38} [{cash_tick}] Cash   [{credit_card_tick}] Credit Card   [{ewallet_tick}] e-Wallet   [{bank_transfer_tick}] Bank Transfer")
                print(f"{'Grand Total:':<90} RM {total_payment:.2f}")
                print(f"{'Deposit:':<90} RM {total_deposit:.2f}")
                print("=" * 100)

            else:
                print("Failed to generate invoice. Please try again.")

        except KeyError as ke:
            print(f"Missing key: {str(ke)}. Please check your data files.")
        except Exception as e:
            print(f"An unexpected error occurred during invoice generation: {str(e)}")

    def process_bank_transfer_payment(self, customer_id):
        try:
            print("\nPlease choose the type of bank transfer: ")
            print("1. MayBank")
            print("2. Public Bank")
            print("3. Bank Islam")
            print("4. Back to Main Menu")

            while True:
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                    self.process_bank_info("MayBank", customer_id)
                    break
                elif choice == "2":
                    self.process_bank_info("Public Bank", customer_id)
                    break
                elif choice == "3":
                    self.process_bank_info("Bank Islam", customer_id)
                    break
                elif choice == "4":
                    self.main()
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 4.")
        except Exception as e:
            print(f"An unexpected error occurred during bank transfer selection: {str(e)}")

    def main(self):
        try:
            if self.read_customer_and_car_data():
                customer_id = self.get_customer_id()
                while True:
                    print("\nPlease select a payment method: ")
                    print("1. Credit Card")
                    print("2. eWallet")
                    print("3. Bank Transfer")
                    print("4. Cash")
                    print("5. Exit")
                    
                    choice = input("Enter your choice: ").strip()
                    
                    if choice == "1":
                        print("\nSelected: Credit Card")
                        self.process_credit_card_payment(customer_id)
                        break
                    elif choice == "2":
                        print("\nSelected: eWallet")
                        self.process_e_wallet_payment(customer_id)
                        break
                    elif choice == "3":
                        print("\nSelected: Bank Transfer")
                        self.process_bank_transfer_payment(customer_id)
                        break
                    elif choice == "4":
                        print("\nSelected: Cash")
                        self.cash_payment(customer_id)
                        break
                    elif choice == "5":
                        print("\nExit.....")
                        break
                    else:
                        print("\nInvalid choice. Please enter a number from 1 to 5.")
            else:
                print("Failed to initialize. Check data files and try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    service = RentalService()
    service.main()