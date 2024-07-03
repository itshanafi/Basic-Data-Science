# open file
# x create the file if it does not exist
# r read only
# w write only
# a append only
# r+ read and write
# w+ write and read
# a+ append and read

'''
file = open("test.txt", "w")
file.write("Hello World")
file.close()

file = open("test.txt", "r")

import os

# if the file already exist and check if will be an error occured in the future
if not os.path.exists("test.txt"):
    try:
        file = open("test.txt", "w")
        file.write("Hello World")
        file.close()
    except Exception as e:
        print(e)
'''


# convert the code into function
import os

def create_file(filename):
    if not os.path.exists(filename):
        try:
            with open(filename, "x") as file:
                file.write("Product | Quantity | Price | Total\n")
        except IOError as e:
            print(f"Error creating file: {e}")
    else:
        print(f"File '{filename}' already exists.")

def add_product(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "a") as file:
                product = input("Enter the product: ")
                quantity = input("Enter the quantity: ")
                price = input("Enter the price (RM): ")
                total = int(quantity) * float(price)
                file.write(f"\n{product} | {quantity} | {price} | {total}")
        except IOError as e:
            print(f"Error adding product: {e}")
    else:
        print(f"File '{filename}' does not exist.")

def read_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                for line in file.readlines():
                    line = line.strip()
                    if line and "|" in line:
                        product, quantity, price, total = line.split("|")
                        print(f"{product.strip():40}{quantity.strip():>20}{price.strip():>20}{total.strip():>20}")
        except IOError as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File '{filename}' does not exist.")

import os

def edit_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r+") as file:
                lines = file.readlines()
                file.seek(0)

                found = False
                for line_index, line in enumerate(lines):
                    line = line.strip()
                    if "|" in line:
                        product, quantity, price, total = line.split("|")
                        print(f"{product.strip():40}{quantity.strip():>20}{price.strip():>20}{total.strip():>20}")

                search_product = input("Enter the product to edit or delete: ").strip().lower()
                edited = False
                for line_index, line in enumerate(lines):
                    if "|" in line:
                        parts = line.strip().split("|")
                        product = parts[0].strip()
                        if product.lower() == search_product:
                            print("\n1. Edit product")
                            print("2. Edit quantity")
                            print("3. Edit price")
                            print("4. Delete product")
                            print("5. Exit")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                new_product = input("Enter the new product: ").strip()
                                parts[0] = new_product
                                edited = True
                                print(f"Product '{product}' has been updated to '{new_product}'.")
                            elif choice == "2":
                                new_quantity = input("Enter the new quantity: ").strip()
                                if new_quantity.isdigit():
                                    parts[1] = new_quantity
                                    edited = True
                                    print(f"Quantity '{quantity}' has been updated to '{new_quantity}'.")
                                else:
                                    print("Invalid input. Quantity must be a number.")
                            elif choice == "3":
                                new_price = input("Enter the new price: ").strip()
                                try:
                                    float(new_price)
                                    parts[2] = new_price
                                    edited = True
                                    print(f"Price '{price}' has been updated to '{new_price}'.")
                                except ValueError:
                                    print("Invalid input. Price must be a number.")
                            elif choice == "4":
                                confirmation = input(f"Are you sure you want to delete '{product}'? (y/n): ").strip().lower()
                                if confirmation == "y":
                                    del lines[line_index]
                                    edited = True
                                    print(f"Product '{product}' has been deleted.")
                                    break  # Exit after deletion
                                else:
                                    print(f"Deletion of '{product}' canceled.")
                            elif choice == "5":
                                print("Exiting...")
                                break
                            else:
                                print("Invalid choice. Try again.")
                                print("")
                            if edited:
                                lines[line_index] = " | ".join(parts) + "\n"
                            break

                if not edited:
                    print(f"Product '{search_product}' not found.")

                file.seek(0)
                file.writelines(lines)
                file.truncate()
        except IOError as e:
            print(f"Error editing file: {e}")
    else:
        print(f"File '{filename}' does not exist.")

def main():
    while True:
        print("1. Create new file")
        print("2. Choose existing file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename to create: ")
            create_file(filename)
            while True:
                print("\nOperations:")
                print("1. Add product")
                print("2. Read file")
                print("3. Edit file")
                print("4. Back to main menu")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    add_product(filename)
                elif sub_choice == "2":
                    read_file(filename)
                elif sub_choice == "3":
                    edit_file(filename)
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Try again.")
        
        elif choice == "2":
            filename = input("Enter the existing filename: ")
            while True:
                if os.path.exists(filename):
                    print("\nOperations:")
                    print("1. Add product")
                    print("2. Read file")
                    print("3. Edit file")
                    print("4. Back to main menu")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        add_product(filename)
                    elif sub_choice == "2":
                        read_file(filename)
                    elif sub_choice == "3":
                        edit_file(filename)
                    elif sub_choice == "4":
                        break
                    else:
                        print("Invalid choice. Try again.")
                else:
                    print(f"File '{filename}' does not exist.")
                    break
        
        elif choice == "3":
            print("\nExiting...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
