import os

class storeManager:
    
    def __init__(self):
        self.filename = None

    def create_file(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            try:
                with open(filename, "x") as file:
                    file.write("Product | Quantity | Price | Total\n")
            except IOError as e:
                print(f"Error creating file: {e}")
        else:
            print(f"File '{filename}' already exists.")

    def add_product(self):
        if self.filename:
            try:
                with open(self.filename, 'a') as f:
                    product = input("Enter the product: ")
                    quantity = int(input("Enter the quantity: "))
                    price = float(input("Enter the price price (RM): ")).strip()
                    total = quantity * price
                    f.write(f"{product} | {quantity} | RM {price} | RM {total}\n")
            except IOError as e:
                print(f"Error adding product: {e}")
        else:
            print(f"File '{self.filename}' does not exist.")

    def read_file(self):
        if self.filename:
            try:
                with open(self.filename, 'r') as f:
                    for line in f.readlines():
                        line = line.strip()
                        if line and '|' in line:
                            product, quantity, price, total = line.split('|')
                            print(f"{product.strip():60}{quantity.strip():>20}{price.strip():>20}{total.strip():>20}")
            except IOError as e:
                print(f"Error reading file: {e}")
        else:
            print(f"File '{self.filename}' does not exist.")

    def edit_file(self):
        if self.filename:
            try:
                with open(self.filename, 'r+') as f:
                    lines = f.readlines()
                    f.seek(0)

                    found = False
                    for line_index, line in enumerate(lines):
                        line = line.strip()
                        
                        if '|' in line:
                            product, quantity, price, total = line.split('|')
                            print(f"{product.strip():40}{quantity.strip():>20}{price.strip():>20}{total.strip():>20}")

                            search_product = input("Enter the name of the product to edit: ")
                            edited = False

                            for line_index, line in enumerate(lines):
                                if '|' in line:
                                    parts = line.strip().split('|')
                                    product = parts[0].strip()

                                    if product.lower() == search_product:
                                        print("\n1. Edit product")
                                        print("2. Edit quantity")
                                        print("3. Edit price")
                                        print("4. Delete product")
                                        print("5. Exit")
                                        
                                        choice = input("Enter your choice: ")
                                        if choice == '1':
                                            new_product = input("Enter the new product: ").strip()
                                            parts[0] = new_product
                                            edited = True
                                            print(f"Product '{product}' has been updated to '{new_product}'.")

                                        elif choice == '2':
                                            new_quantity = input("Enter the new quantity: ").strip()
                                            if new_quantity.isdigit():
                                                parts[1] = new_quantity
                                                edited = True
                                                print(f"Quantity '{quantity}' was updated to '{new_quantity}'.")
                                                
                                            else:
                                                print("Invalid input. Quantity must be in number.")

                                        elif choice == '3':
                                            new_price = input("Enter the new price: ").strip()
                                            try:
                                                float(new_price)
                                                parts[2] = new_price
                                                edited = True
                                                print(f"Price '{price}' has been updated to '{new_price}'.")
                                            except ValueError:
                                                print("Invalid input. Price must be a number.")

                                        elif choice == '4':
                                            confirmation = input(f"Are you sure you want to delete '{product}'? (y/n): ").strip().lower()
                                            if confirmation == "y":
                                                del lines[line_index]
                                                edited = True
                                                print(f"Product '{product}' has been deleted.")
                                                break  # Exit after deletion

                                            elif confirmation == "n":
                                                print(f"Deletion of '{product}' canceled.")

                                            else:
                                                print("Invalid choice. Try again.")

                                        elif choice == '5':
                                            print("Exiting...")
                                            break

                                        else:
                                            print("Invalid choice. Try again.")
                                            print("")

                                        if edited:
                                            lines[line_index] = ' | '.join(parts) + '\n'
                                            break

                            if not edited:
                                print(f"Product '{search_product}' not found.")

                            f.seek(0)
                            f.writelines(lines)
                            f.truncate()

            except IOError as e:
                print(f"Error editing file: {e}")

        else:
            print(f"File '{self.filename}' does not exist.")

    def mainMenu(self):
        while True:
            print("\n1. Create new file")
            print("2. Choose existing file")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                filename = input("Enter the filename to create: ")
                self.create_file(filename)
                self.inventory_operation_menu()

            elif choice == '2':
                filename = input("Enter the existing filename: ")

                if os.path.exists(filename):
                    self.filename = filename
                    self.inventory_operation_menu()

                else:
                    print(f"File '{filename}' does not exist")

            elif choice == '3':
                print("\nExiting...")
                break

            else:
                print("Invalid input. Try again.")

    def inventory_operation_menu(self):
        while True:
            print("\nOperations:")
            print("1. Add product")
            print("2. Read file")
            print("3. Edit file")
            print("4. Back to main menu")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                self.add_product()

            elif sub_choice == '2':
                self.read_file()

            elif sub_choice == '3':
                self.edit_file()

            elif sub_choice == '4':
                break

            else:
                print("Invalid choice. Try again.")

if __name__ == '__main__':
    storeManager = storeManager()
    storeManager.mainMenu()