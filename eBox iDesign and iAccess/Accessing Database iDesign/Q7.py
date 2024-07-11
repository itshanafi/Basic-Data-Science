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
import sys
from mysql.connector import Error
from prettytable import PrettyTable

# Reading database configuration from 'mysql.properties' file
config = configparser.RawConfigParser()
config.read('mysql.properties')

dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

def insert_item_type(cursor, item_type_name, deposit, cost_per_day):
    query = "INSERT INTO item_type (item_type_name, deposit, cost_per_day) VALUES (%s, %s, %s)"
    cursor.execute(query, (item_type_name, deposit, cost_per_day))

def insert_item_details(cursor, id, item_name, vendor_name, item_type_name, deposit, cost_per_day):
    query = "INSERT INTO item_details (id, item_name, vendor_name, item_type_name, deposit, cost_per_day) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id, item_name, vendor_name, item_type_name, deposit, cost_per_day))

def display_table(cursor, table_name, fields):
    query = f"SELECT {', '.join(fields)} FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    table = PrettyTable()
    table.field_names = fields
    
    for row in rows:
        table.add_row(row)
    
    print(table)

try:
    # Establishing the connection to the database
    connection = mysql.connector.connect(
        host=dburl,
        database=dbname,
        user=username,
        password=password,
        port=port
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Displaying the current item_type table
        display_table(cursor, "item_type", ["item_type_name", "deposit", "cost_per_day"])
        
        # Asking user if they want to add new ItemTypes
        while True:
            print("Do you want to add new ItemType? (Y/N)")
            add_item_type = input().strip().upper()
            if add_item_type == 'N':
                break
            elif add_item_type == 'Y':
                print("Enter number of itemtype details")
                num_item_types = int(input().strip())
                for i in range(num_item_types):
                    print(f"Enter itemtype {i + 1} details in CSV format (item_type_name, deposit, cost_per_day):")
                    item_type_details = input().split(',')
                    item_type_name = item_type_details[0].strip()
                    deposit = float(item_type_details[1].strip())
                    cost_per_day = float(item_type_details[2].strip())
                    insert_item_type(cursor, item_type_name, deposit, cost_per_day)
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        
        connection.commit()
        
        # Displaying the updated item_type table
        display_table(cursor, "item_type", ["item_type_name", "deposit", "cost_per_day"])
        
        # Getting item details from the user
        print("Enter number of item details")
        num_items = int(input().strip())
        for i in range(num_items):
            print(f"Enter the item {i + 1} details in CSV format (id, item_name, vendor_name, item_type_name, deposit, cost_per_day):")
            item_details = input().split(',')
            id = int(item_details[0].strip())
            item_name = item_details[1].strip()
            vendor_name = item_details[2].strip()
            item_type_name = item_details[3].strip()
            deposit = float(item_details[4].strip())
            cost_per_day = float(item_details[5].strip())
            insert_item_details(cursor, id, item_name, vendor_name, item_type_name, deposit, cost_per_day)
        
        connection.commit()
        
        # Displaying the updated item_details table
        display_table(cursor, "item_details", ["id", "item_name", "vendor_name", "item_type_name", "deposit", "cost_per_day"])
        
except Error as e:
    print(f"Error: {e}")
    sys.exit(1)
finally:
    # Closing the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
