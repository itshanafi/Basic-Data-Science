import ast
import datetime
import time
import os

class CarRentalSystem:
    def __init__(self):
        self.customers_data = {}
        self.cars_data = {}
    
    def read_customer_and_car_data(self):
        try:
            if not os.path.exists('Customer Detail.txt') or not os.path.exists('Car Detail.txt'):
                raise FileNotFoundError("One or both data files not found.")
            
            with open('Customer Detail.txt', 'r') as customer_file:
                customer_content = customer_file.read().strip()
                self.customers_data = ast.literal_eval(customer_content)
            
            with open('Car Detail.txt', 'r') as car_file:
                car_content = car_file.read().strip()
                self.cars_data = ast.literal_eval(car_content)
            
            return True
        
        except FileNotFoundError:
            print("Error: One or both data files not found.")
            return False
        
        except ValueError:
            print("Error: Failed to parse data from one or both files.")
            return False
        
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return False

    
    def display_customer_and_car(self, customer_id):
        if customer_id in self.customers_data:
            customer = self.customers_data[customer_id]
            print(f"Customer ID: {customer_id}")
            car_id = customer.get('CarID')  # Using .get() for safer key access
            if car_id in self.cars_data:
                car = self.cars_data[car_id]
                return customer, car
            else:
                print(f"Car details not found for CarID: {car_id}")
                return None, None
        else:
            print(f"Customer ID '{customer_id}' not found.")
            return None, None
    
    def calculate_deposit(self, customer, car):
        try:
            start_date = datetime.datetime.strptime(customer['Startdate'], "%Y-%m-%d")
            end_date = datetime.datetime.strptime(customer['Enddate'], "%Y-%m-%d")
            rental_days = (end_date - start_date).days + 1
            
            price_per_day = float(car['Price/day'].replace("RM", ""))
            total_deposit = (rental_days * price_per_day) // 3
            
            return total_deposit
        
        except ValueError:
            print("Error: Failed to calculate deposit due to invalid value.")
            return None
        except ZeroDivisionError:
            print("Error: Division by zero error in deposit calculation.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return None

    
    def calculate_payment(self, customer, car):
        try:
            start_date = datetime.datetime.strptime(customer['Startdate'], "%Y-%m-%d")
            end_date = datetime.datetime.strptime(customer['Enddate'], "%Y-%m-%d")
            rental_days = (end_date - start_date).days + 1
            
            price_per_day = float(car['Price/day'].replace("RM", ""))
            total_payment = rental_days * price_per_day
            
            return total_payment
        
        except ValueError:
            print("Error: Failed to calculate payment.")
            return None
    
    def get_customer_id(self):
        while True:
            try:
                customer_id = input("Enter Customer ID: ").strip()
                if customer_id in self.customers_data:
                    return customer_id
                else:
                    print(f"Customer ID '{customer_id}' not found. Please enter a valid ID.")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                return None

    
    def make_payment(self, wallet_name):
        customer_id = self.get_customer_id()
        
        if customer_id:
            customer, car = self.display_customer_and_car(customer_id)
            
            if customer and car:
                total_payment = self.calculate_payment(customer, car)
                if total_payment is not None:
                    try:
                        current_balance = float(customer['Balance'].replace("RM", ""))
                        
                        if current_balance >= total_payment:
                            new_balance = current_balance - total_payment
                            self.customers_data[customer_id]['Balance'] = f"RM{new_balance:.2f}"
                            print(f"Total Payment: RM {total_payment:.2f}")
                            print(f"Remaining Balance: RM {new_balance:.2f}")
                            self.confirm_payment(wallet_name, customer_id)
                            return True
                        else:
                            print("Insufficient balance. Please choose another payment method.")
                            return False
                    except ValueError:
                        print("Error: Failed to process payment due to invalid balance.")
                        return False
                    except Exception as e:
                        print(f"An unexpected error occurred: {str(e)}")
                        return False
            else:
                print(f"Failed to make payment for Customer ID '{customer_id}'. Please try again.")
                return False
        else:
            print("Invalid customer ID. Please try again.")
            return False

    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def card_info(self):
        customer_id = self.get_customer_id()
        
        if customer_id:
            print("\nEnter the card number (16 digits): ")
            card_number = input().replace(" ", "").strip()
            if len(card_number) != 16 or not card_number.isdigit():
                print("\nInvalid card number format. Please enter a valid 16-digit number.")
                return
            
            print("\nEnter the card holder name: ")
            card_holder_name = input().strip()
    
            print("\nEnter the expiry date (MMYY): ")
            expiry_date = input().replace('/', '').strip()
            if len(expiry_date) != 4 or not expiry_date.isdigit():
                print("\nInvalid expiry date format. Please enter MMYY.")
                return
            
            month = int(expiry_date[:2])
            year = int(expiry_date[2:])
            current_year = datetime.datetime.now().year % 100
            
            if year < current_year or (year == current_year and month < datetime.datetime.now().month):
                print("\nInvalid expiry date. Please enter a future date.")
                return
    
            print("\nEnter the CVV / CVC (3 digits): ")
            cvv = input().strip()
            if len(cvv) != 3 or not cvv.isdigit():
                print("\nInvalid CVV format. Please enter a valid 3-digit number.")
                return
    
            print("\nProcessing... Please wait...")
            time.sleep(2)  # Simulating processing time
            self.clear_screen()  # Clear the screen before displaying success message
    
            print("\nYour payment has been successful!")
            print(f"Card Number: {'*' * 12}{card_number[-4:]}")
            print(f"Card Holder: {card_holder_name}")
            print(f"Expiry Date: {expiry_date[:2]}/{expiry_date[2:]}")
            
            self.confirm_payment("Credit Card", customer_id)
    
    def e_wallet(self):
        customer_id = self.get_customer_id()
        
        if customer_id:
            print(f"\nSelected: eWallet")
            print(f"Customer ID entered: {customer_id}")
            
            if customer_id in self.customers_data:
                customer = self.customers_data[customer_id]
                car_id = customer.get('CarID')
                
                if car_id in self.cars_data:
                    car = self.cars_data[car_id]
                    total_deposit = self.calculate_deposit(customer, car)
                    
                    if total_deposit is not None:
                        current_balance = float(customer['Balance'].replace("RM", ""))
                        
                        if current_balance >= total_deposit:
                            new_balance = current_balance - total_deposit
                            self.customers_data[customer_id]['Balance'] = f"RM{new_balance:.2f}"
                            print(f"Total Payment: RM {total_deposit:.2f}")
                            print(f"Remaining Balance: RM {new_balance:.2f}")
                            self.confirm_payment("eWallet", customer_id)
                            return True
                        else:
                            print("Insufficient balance. Please choose another payment method.")
                            return False
                else:
                    print(f"Car with ID '{car_id}' not found in cars data. Please try again.")
                    return False
            else:
                print(f"Customer with ID '{customer_id}' not found in customers data. Please try again.")
                return False
    
    def bank_transfer(self):
        customer_id = self.get_customer_id()
        
        if customer_id:
            print("\nPlease choose the type of bank transfer: ")
            print("1. MayBank")
            print("2. Public Bank")
            print("3. Bank Islam")
            print("4. Exit")
            
            while True:
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                    self.bank_info("MayBank", customer_id)
                    break
                elif choice == "2":
                    self.bank_info("Public Bank", customer_id)
                    break
                elif choice == "3":
                    self.bank_info("Bank Islam", customer_id)
                    break
                elif choice == "4":
                    print("\nExit.....")
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 4.")
    
    def bank_info(self, bank_name, customer_id):
        print(f"\nSelected: {bank_name}")
        print("\nPlease Enter Your Username: ")
        username = input().strip()
        print("\nPlease Enter Your Password: ")
        password = input().strip()  # Handle password securely if storing is required
    
        print("\nProcessing... Please wait...")
        time.sleep(3)  # Simulating processing time
        self.clear_screen()  # Clear the screen before displaying success message
        print("Payment confirmed!")
        
        self.confirm_payment(bank_name, customer_id)
    
    def confirm_payment(self, wallet_name, customer_id):
        print(f"\nYou have selected {wallet_name} for payment.")
        print("Please confirm your payment details.")
        time.sleep(5)  # Simulating processing time
        self.clear_screen()  # Clear the screen before displaying success message
        print("Payment confirmed!")
        self.display_invoice(customer_id)
    
    def display_invoice(self, customer_id):
        customer, car = self.display_customer_and_car(customer_id)
        
        if customer and car:
            total_payment = self.calculate_payment(customer, car)
            total_deposit = self.calculate_deposit(customer, car)
            if total_payment is not None and total_deposit is not None:
                self.clear_screen()
                line_width = 50
                title = "Invoice"
                title_length = len(title)
                remaining_space = (line_width - title_length) // 2
                print("=" * line_width)
                print(f"{' ' * remaining_space}{title}{' ' * remaining_space}")
                print("=" * line_width)
                
                print(f"Customer ID: {customer_id}")
                print(f"Customer Name: {customer['Name']}")
                print("-" * line_width)
                print(f"Car ID: {customer['CarID']}")
                print(f"Car Model: {car['Type']}")
                print(f"Rental Period: {customer['Startdate']} to {customer['Enddate']}")
                print("-" * line_width)
                print(f"{'Total Deposit:':<40} RM {total_deposit:.2f}")
                print(f"{'Total Payment:':<40} RM {total_payment:.2f}")
                print("=" * line_width)
        else:
            print("Failed to generate invoice. Customer or car details not found.")
    
    def main(self):
        try:
            if self.read_customer_and_car_data():
                while True:
                    print("\nPlease select a payment method: ")
                    print("1. Credit Card")
                    print("2. eWallet")
                    print("3. Bank Transfer")
                    print("4. Exit")
                    
                    choice = input("Enter your choice: ").strip()
                    
                    if choice == "1":
                        print("\nSelected: Credit Card")
                        self.card_info()
                        break
                    
                    elif choice == "2":
                        print("\nSelected: eWallet")
                        self.e_wallet()
                        break
                    
                    elif choice == "3":
                        print("\nSelected: Bank Transfer")
                        self.bank_transfer()
                        break
                    
                    elif choice == "4":
                        print("\nExit.....")
                        break
                    
                    else:
                        print("\nInvalid choice. Please enter a number from 1 to 4.")
            else:
                print("Failed to initialize. Check data files and try again.")

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    car_rental_system = CarRentalSystem()
    car_rental_system.main()
