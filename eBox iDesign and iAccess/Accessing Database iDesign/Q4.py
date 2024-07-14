# Write a program to execute a query to display the details of a user from the 'user' table in a MySql database
# and also update contact details and display the details for that user.
# In this program, display the user table first and prompt the user to provide a username.
# If the username is present in the user table, get the contact details to be updated and update it in the user table.
# Otherwise, Display an error message.
# Table Schema:
# Note: 
# For display, the result set use PrettyTable 
# For example : 
# from prettytable import PrettyTable.
# x = PrettyTable() 
# x.add_row([....]) #Use this for add all the rows 
# print x #To print the final result set  
# [All text in bold corresponds to the input and rest corresponds to the output]
# Sample Input and Output 1:
# +----+-------+----------------+-----------+----------+
# | Id |  Name | Contact Detail |  Username | Password |
# +----+-------+----------------+-----------+----------+
# | 1  |  John |   9876543210    |   johny   |  12345   |
# | 2  | Peter |   9873216540   |  peterey  |  pet123  |
# | 3  |  Adam |   9871236504   |  adamanta |  ad@123  |
# | 4  | Linda |   8794561320   | lindahere |   abcd   |
# | 5  |  Tony |   7894561230   |   tonii   |  abc123  |
# +----+-------+----------------+-----------+----------+
# Enter the username:
# John
# +----+------+----------------+----------+----------+
# | Id | Name | Contact Detail | Username | Password |
# +----+------+----------------+----------+----------+
# | 1  | John |   9876543210   |  johny   |  12345   |
# +----+------+----------------+----------+----------+
# Enter the mobile number to be updated:
# 9621675431
# +----+------+----------------+----------+----------+
# | Id | Name | Contact Detail | Username | Password |
# +----+------+----------------+----------+----------+
# | 1  | John |   9621675431   |  johny   |  12345   |
# +----+------+----------------+----------+----------+
# Sample Input and Output 2:
# +----+-------+----------------+-----------+----------+
# | Id |  Name | Contact Detail |  Username | Password |
# +----+-------+----------------+-----------+----------+
# | 1  |  John |   9620685431   |   johny   |  12345   |
# | 2  | Peter |   9873216540   |  peterey  |  pet123  |
# | 3  |  Adam |   9871236504   |  adamanta |  ad@123  |
# | 4  | Linda |   8794561320   | lindahere |   abcd   |
# | 5  |  Tony |   7894561230   |   tonii   |  abc123  |
# +----+-------+----------------+-----------+----------+
# Enter the username:
# admin
# No such user is present


import mysql.connector
import configparser
from prettytable import PrettyTable
from mysql.connector import Error

# Read database configuration from properties file
config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

# Function to connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=dburl,
            database=dbname,
            user=username,
            password=password,
            port=port
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

# Function to display the user table
def display_user_table(cursor):
    cursor.execute("SELECT * FROM user")
    records = cursor.fetchall()
    table = PrettyTable(["Id", "Name", "Contact Detail", "Username", "Password"])
    for row in records:
        table.add_row(row)
    print(table)

# Function to update contact details for a given name
def update_contact_details(cursor, connection, name):
    cursor.execute("SELECT * FROM user WHERE name = %s", (name,))
    record = cursor.fetchone()
    if record:
        table = PrettyTable(["Id", "Name", "Contact Detail", "Username", "Password"])
        table.add_row(record)
        print(table)
        print("Enter the mobile number to be updated:")
        new_contact = input()
        cursor.execute("UPDATE user SET contactDetail = %s WHERE name = %s", (new_contact, name))
        connection.commit()

        cursor.execute("SELECT * FROM user WHERE name = %s", (name,))
        updated_record = cursor.fetchone()
        table = PrettyTable(["Id", "Name", "Contact Detail", "Username", "Password"])
        table.add_row(updated_record)
        print(table)
    else:
        print("No such user is present")

# Main function
def main():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()

        # Display the user table
        display_user_table(cursor)

        # Prompt user for a name
        print("Enter the username:")
        user_input = input()
        
        # Update contact details for the given name
        update_contact_details(cursor, connection, user_input)

        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
