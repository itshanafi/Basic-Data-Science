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

# Load database configuration from 'mysql.properties'
config = configparser.RawConfigParser()
config.read('mysql.properties')
db_host = config.get('DatabaseSection', 'db.host')
db_name = config.get('DatabaseSection', 'db.schema')
db_username = config.get('DatabaseSection', 'db.username')
db_password = config.get('DatabaseSection', 'db.password')

def display_users(cursor):
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    table = PrettyTable(['Id', 'Name', 'Contact Detail', 'Username', 'Password'])
    for row in rows:
        table.add_row(row)
    print(table)

def get_user(cursor, name):
    cursor.execute("SELECT * FROM user WHERE name = %s", (name,))
    return cursor.fetchone()

def display_user_details(user):
    table = PrettyTable(['Id', 'Name', 'Contact Detail', 'Username', 'Password'])
    table.add_row(user)
    print(table)

def update_contact_detail(cursor, connection, user_id, new_contact_detail):
    cursor.execute("UPDATE user SET contactDetail = %s WHERE id = %s", (new_contact_detail, user_id))
    connection.commit()

try:
    # Connect to the database
    connection = mysql.connector.connect(
        host=db_host,
        database=db_name,
        user=db_username,
        password=db_password
    )
    if connection.is_connected():
        cursor = connection.cursor()

        # Display the user table
        display_users(cursor)

        # Prompt for username
        print("Enter the username:")
        name = input()

        # Check if the user exists
        user = get_user(cursor, name)
        if user:
            # Display user details
            display_user_details(user)
            
            new_contact_detail = input()
            update_contact_detail(cursor, connection, user[0], new_contact_detail)
            
            # Display the updated user details
            updated_user = get_user(cursor, name)
            display_user_details(updated_user)
        else:
            print("No such user is present")

except mysql.connector.Error as error:
    print(f"Error: {error}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
