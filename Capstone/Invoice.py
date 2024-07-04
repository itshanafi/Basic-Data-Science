import ast

def display_customer_and_car(customer_id):
    try:
        # Read Customer Detail.txt
        with open('Customer Detail.txt', 'r') as customer_file:
            customers_data = ast.literal_eval(customer_file.read())
        
        # Read Car Detail.txt
        with open('Car Detail.txt', 'r') as car_file:
            cars_data = ast.literal_eval(car_file.read())
        
        # Check if customer_id exists in customers_data
        if customer_id in customers_data:
            # Retrieve customer details
            customer = customers_data[customer_id]
            print(f"Customer ID: {customer_id}")
            print(f"Name: {customer['Name']}")
            print(f"Address: {customer['Address']}")
            print(f"Phone: {customer['Phone']}")
            print(f"IC No: {customer['IC No']}")
            print(f"Balance: {customer['Balance']}")
            print(f"Start Date: {customer['Startdate']}")
            print(f"End Date: {customer['Enddate']}")
            
            # Retrieve car details using CarID from customer data
            car_id = customer['CarID']
            if car_id in cars_data:
                car = cars_data[car_id]
                print("\nCar Details:")
                print(f"Brand: {car['Brand']}")
                print(f"Type: {car['Type']}")
                print(f"Plate Number: {car['Plate Num']}")
                print(f"Price per Day: {car['Price/day']}")
            else:
                print(f"\nCar details not found for CarID: {car_id}")
        else:
            print(f"Customer ID '{customer_id}' not found.")
    
    except FileNotFoundError:
        print("Error: One or both data files not found.")
    except ValueError:
        print("Error: Failed to parse data from one or both files.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage:
customer_id = "001"
display_customer_and_car(customer_id)
