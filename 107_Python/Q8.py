# Write a Python class Inventory with attributes like id, productName, availableQuantity and price.
# Add methods like addItem, updateItem, and checkItem_details.
# Use a dictionary to store the item details, where the key is the id and the value
# is a dictionary containing the productName, availableQuantity and price.
# Sample Data:
# {
#   "97410": {
#     "name": "Television",
#     "availableQuantity": 20,
#     "price": 1455.99
#   },
#   "97411": {
#     "name": "Radio",
#     "availableQuantity": 32,
#     "price": 654.25
#   }
# }

class Inventory:
    def __init__(self, initial_data=None):
        self.inventory = {}
        if initial_data:
            for id, details in initial_data.items():
                self.inventory[id] = {
                    "name": details["name"],
                    "availableQuantity": details["availableQuantity"],
                    "price": details["price"]
                }

    def addItem(self):
        print("\nAdd Item")
        id = input("Enter the id: ")
        name = input("Enter the name: ")
        availableQuantity = int(input("Enter the availableQuantity: "))
        price = float(input("Enter the price: "))
        self.inventory[id] = {"name": name, "availableQuantity": availableQuantity, "price": price}
        print(f"Item with ID {id} added successfully.")

    def updateItem(self, id):
        if id in self.inventory:
            print(f"\nUpdate Item with ID {id}")
            name = input("Enter the new name: ")
            availableQuantity = int(input("Enter the new availableQuantity: "))
            price = float(input("Enter the new price: "))
            self.inventory[id] = {"name": name, "availableQuantity": availableQuantity, "price": price}
            print(f"Item with ID {id} updated successfully.")
        else:
            print("Item not found.")

    def checkItem_details(self, id):
        if id in self.inventory:
            print("\nItem details:")
            print("Name:", self.inventory[id]["name"])
            print("Available Quantity:", self.inventory[id]["availableQuantity"])
            print("Price:", self.inventory[id]["price"])
        else:
            print("Item not found.")

def main():
    # Sample Data
    initial_data = {
        "97410": {
            "name": "Television",
            "availableQuantity": 20,
            "price": 1455.99
        },
        "97411": {
            "name": "Radio",
            "availableQuantity": 32,
            "price": 654.25
        }
    }

    inventory = Inventory(initial_data)
    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Check Item details")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            inventory.addItem()
        elif choice == '2':
            id = input("Enter the id of the item to update: ")
            inventory.updateItem(id)
        elif choice == '3':
            id = input("Enter the id of the item to check details: ")
            inventory.checkItem_details(id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
