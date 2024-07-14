# Write a program to execute a query for adding multiple details and displaying all details in the respective table.
# In this program, insert multiple details ItemType in 'item_type' table and Item details in 'item_details' to their, in MySQL database.
# Table Name :
# ‘item_type’
# Attributes : item_type(
# item_type_name VARCHAR(45) ,
# deposit    DOUBLE ,
# cost_per_day DOUBLE );
# ‘item_details’
# Attributes : item_details(
# id bigint    ,
# item_name VARCHAR(45)  ,
# vendor_name VARCHAR(45)  ,
# item_type_name VARCHAR(45)  ,
# deposit    DOUBLE  ,
# cost_per_day DOUBLE  );
# Note: 
# For display, the result set use PrettyTable 
# For example : 
# from prettytable import PrettyTable.
# x = PrettyTable() 
# x.add_row([....]) #Use this for add all the rows 
# print x #To print the final result set 
# [All text in bold corresponds to the input and rest corresponds to the output]
# Sample Input and Output 1:
# +---------------+---------+--------------+
# | ItemType name | Deposit | Cost per day |
# +---------------+---------+--------------+
# |      Food     | 50000.0 |   10000.0    |
# |  Electronics  | 85000.0 |   15000.0    |
# |    Fashion    | 36000.0 |    8000.0    |
# |    Grooming   | 15000.0 |    5000.0    |
# +---------------+---------+--------------+
# Do you want to add new ItemType? (Y/N)
# N
# Enter number of item details
# 0
# +----+------------------+----------------------+---------------+---------+--------------+
# | Id |    Item name     |     Vendor name      | ItemType name | Deposit |Cost per day |
# +----+------------------+----------------------+---------------+---------+--------------+
# | 1  |    Chocolate     |    Foodies  Court    |      Food     | 50000.0 |   10000.0    |
# | 2  |     Lollypop     |    Foodies  Court    |      Food     | 50000.0 |   10000.0    |
# | 3  |   Mobile phone   |   MP  electronics    |  Electronics  | 85000.0 |   15000.0    |
# | 4  |      Laptop      |   AMP  electronics   |  Electronics  | 85000.0 |   15000.0    |
# | 5  |   Titan watch    | Tata watch  paradise |    Fashion    | 36000.0 |   8000.0    |
# | 6  |   Sonata watch   | Tata watch  paradise |    Fashion    | 36000.0 | 8000.0    |
# | 7  | Phillips Trimmer |   Reliance  Trendz   |    Grooming   | 15000.0 |   5000.0    |
# | 8  |   Nova Shaver    |   Reliance  Trendz   |    Grooming   | 15000.0 |   5000.0    |
# | 9  |     Let us C     |   Einstien  Books    |     Books     | 20000.0 |   7500.0    |
# | 10 |       OOPS       |   Einstien  Books    |     Books     | 20000.0 |   7500.0    |
# +----+------------------+----------------------+---------------+---------+--------------+
# Sample Input and Output 2:
# +---------------+---------+--------------+
# | ItemType name | Deposit | Cost per day |
# +---------------+---------+--------------+
# |      Food     | 50000.0 |   10000.0    |
# |  Electronics  | 85000.0 |   15000.0    |
# |    Fashion    | 36000.0 |    8000.0    |
# |    Grooming   | 15000.0 |    5000.0    |
# |     Books     | 20000.0 |    7500.0    |
# +---------------+---------+--------------+
# Do you want to add new ItemType? (Y/N)
# Y
# Enter number of itemtype details
# 1
# Enter itemtype 1 details in CSV format
# Electrical,10000,2000
# Enter number of item details
# 2
# Enter the item 1 details in CSV format
# Multimeter,JK electricals,Electrical
# Enter the item 2 details in CSV format
# Encyclopedia,Einstein Books,Books
# +----+------------------+----------------------+---------------+---------+--------------+
# | Id |    Item name     |     Vendor name      | ItemType name | Deposit | Cost per day |
# +----+------------------+----------------------+---------------+---------+--------------+
# | 1  |    Chocolate     |    Foodies  Court    |      Food     | 50000.0 |   10000.0    |
# | 2  |     Lollypop     |    Foodies  Court    |      Food     | 50000.0 |   10000.0    |
# | 3  |   Mobile phone   |   MP  electronics    |  Electronics  | 85000.0 |   15000.0    |
# | 4  |      Laptop      |   AMP  electronics   |  Electronics  | 85000.0 |   15000.0    |
# | 5  |   Titan watch    | Tata watch  paradise |    Fashion    | 36000.0 |   8000.0    |
# | 6  |   Sonata watch   | Tata watch  paradise |    Fashion    | 36000.0 |   8000.0    |
# | 7  | Phillips Trimmer |   Reliance  Trendz   |    Grooming   | 15000.0 |   5000.0    |
# | 8  |   Nova Shaver    |   Reliance  Trendz   |    Grooming   | 15000.0 |   5000.0    |
# | 9  |     Let us C     |   Einstien  Books    |     Books     | 20000.0 |   7500.0    |
# | 10 |       OOPS       |   Einstien  Books    |     Books     | 20000.0 |   7500.0    |
# | 11 |    Multimeter    |    JK electricals    |   Electrical  | 10000.0 |   2000.0    |
# | 12 |   Encyclopedia   |    Einstein Books    |     Books     | 20000.0 |   7500.0    |
# +----+------------------+----------------------+---------------+---------+--------------+

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

# Function to insert a new item type
def insert_item_type(cursor, item_type):
    query = "INSERT INTO item_type (item_type_name, deposit, cost_per_day) VALUES (%s, %s, %s)"
    cursor.execute(query, item_type)

# Function to insert a new item detail
def insert_item_detail(cursor, item_detail):
    query = "INSERT INTO item_details (id, item_name, vendor_name, item_type_name, deposit, cost_per_day) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, item_detail)

# Function to fetch and display details from item_type table
def display_item_types(cursor):
    query = "SELECT * FROM item_type"
    cursor.execute(query)
    records = cursor.fetchall()
    table = PrettyTable(["ItemType name", "Deposit", "Cost per day"])
    for row in records:
        table.add_row(row)
    print(table)

# Function to fetch and display details from item_details table
def display_item_details(cursor):
    query = "SELECT * FROM item_details"
    cursor.execute(query)
    records = cursor.fetchall()
    table = PrettyTable(["Id", "Item name", "Vendor name", "ItemType name", "Deposit", "Cost per day"])
    for row in records:
        table.add_row(row)
    print(table)

# Main function
def main():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        
        # Display current item types
        display_item_types(cursor)

        # Ask the user if they want to add new item types
        print("Do you want to add new ItemType? (Y/N)")
        add_item_type = input()
        if add_item_type.upper() == 'Y':
            print("Enter number of itemtype details")
            num_item_types = int(input())
            for i in range(num_item_types):
                print("Enter itemtype {i+1} details in CSV format")
                item_type_details = input()
                item_type = tuple(item_type_details.split(','))
                insert_item_type(cursor, item_type)
        
        # Ask the user how many item details they want to add
        print("Enter number of item details")
        num_item_details = int(input())
        if num_item_details > 0:
            for i in range(num_item_details):
                print("Enter the item {i+1} details in CSV format")
                item_details_str = input()
                item_detail = tuple(item_details_str.split(','))
                insert_item_detail(cursor, item_detail)

            connection.commit()
        
        # Display updated item details
        display_item_details(cursor)

        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
