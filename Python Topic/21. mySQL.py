import mysql.connector as mysql

def dbConnect():
    connection = mysql.connect(
        host="localhost",
        user="root",
        password='',
        database="peneraju"
    )
    return connection

def add_product(connection):
    product = str(input("Enter the product: "))
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price (RM): "))
    description = str(input("Enter the description of the item: "))

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO products (name, description, quantity, price) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (product, description, quantity, price))
        connection.commit()
        print("Product added successfully.")
    except mysql.Error as e:
        print(f"Error adding product: {e}")

def read_file(connection):
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM products"
        cursor.execute(sql)
        result = cursor.fetchall()

        # Print headers
        print(f"{'ID':<6} | {'Name':<20} | {'Description':<40} | {'Quantity':<20} | {'Price':<20}")

        # Print each row
        for row in result:
            print(f"{row[0]:<6} | {row[1]:<20} | {row[2]:<40} | {row[3]:<20} | {row[4]:<20}")
    except mysql.Error as e:
        print(f"Error reading products: {e}")

def edit_file(connection):
    try:
        cursor = connection.cursor(buffered=True)
        sql = "SELECT * FROM products"
        cursor.execute(sql)
        result = cursor.fetchall()

        print(f"{'ID':<6} | {'Name':<20} | {'Description':<40} | {'Quantity':<20} | {'Price':<20}")

        for row in result:
            print(f"{row[0]:<6} | {row[1]:<20} | {row[2]:<40} | {row[3]:<20} | {row[4]:<20}")

        search_product = input("Enter the product ID to edit or delete: ").strip().lower()
        edited = False
        for row in result:
            if str(row[0]) == search_product:
                print("\n1. Edit product")
                print("2. Edit quantity")
                print("3. Edit price")
                print("4. Edit description")
                print("5. Delete product")
                print("6. Exit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    new_product = input("Enter the new product: ").strip()
                    sql = "UPDATE products SET name = %s WHERE id = %s"
                    cursor.execute(sql, (new_product, search_product))
                    connection.commit()
                    edited = True
                    print(f"Product '{row[1]}' has been updated to '{new_product}'.")
                elif choice == "2":
                    new_quantity = input("Enter the new quantity: ").strip()
                    sql = "UPDATE products SET quantity = %s WHERE id = %s"
                    cursor.execute(sql, (new_quantity, search_product))
                    connection.commit()
                    edited = True
                    print(f"Quantity '{row[3]}' has been updated to '{new_quantity}'.")
                elif choice == "3":
                    new_price = input("Enter the new price: ").strip()
                    sql = "UPDATE products SET price = %s WHERE id = %s"
                    cursor.execute(sql, (new_price, search_product))
                    connection.commit()
                    edited = True
                    print(f"Price '{row[4]}' has been updated to '{new_price}'.")
                elif choice == "4":
                    new_description = input("Enter the new description: ").strip()
                    sql = "UPDATE products SET description = %s WHERE id = %s"
                    cursor.execute(sql, (new_description, search_product))
                    connection.commit()
                    edited = True
                    print(f"Description '{row[2]}' has been updated to '{new_description}'.")
                elif choice == "5":
                    confirmation = input(f"Are you sure you want to delete '{row[1]}'? (y/n): ").strip().lower()
                    if confirmation == "y":
                        sql = "DELETE FROM products WHERE id = %s"
                        cursor.execute(sql, (search_product,))
                        connection.commit()
                        edited = True
                        print(f"Product '{row[1]}' has been deleted.")
                        break
                    else:
                        print(f"Deletion of '{row[1]}' canceled.")
                elif choice == "6":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Try again.")
                    print("")
                break

        if not edited:
            print(f"Product with ID '{search_product}' not found.")

    except mysql.Error as e:
        print(f"Error editing products: {e}")

def main():
    connection = dbConnect()
    while True:
        print("\nOperations:")
        print("1. Add product")
        print("2. Read products")
        print("3. Edit products")
        print("4. Exit")
        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":
            add_product(connection)
        elif sub_choice == "2":
            read_file(connection)
        elif sub_choice == "3":
            edit_file(connection)
        elif sub_choice == "4":
            break
        else:
            print("Invalid choice.")

    connection.close()

if __name__ == "__main__":
    main()
