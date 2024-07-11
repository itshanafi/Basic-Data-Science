# Write a program to execute a query to display the details for an Item from the 'item' table and
#     also display the given category details from the 'category' table, in the MySql database. 
# In this program, you have to use the SELECT statement with WHERE condition to fetch records from a table.
# WHERE condition is used to choose the records based on the given condition. Prompt the user for a
# Category Name present in the ItemType table. Display the records of Items that have the item type name given by the user. 
# Table name :
# ‘item’
# Attributes :item(
# id bigint ,
# name VARCHAR(45) ,
# deposit    DOUBLE ,
# cost_per_day DOUBLE);
# ‘category’
# Attributes : category(
# id bigint ,
# name VARCHAR(45) ,
# type_id    int,
# vendor VARCHAR(45) );
# Note: 
# For display the result set use PrettyTable 
# For example : 
# from prettytable import PrettyTable.
# x = PrettyTable() 
# x.add_row([....]) #Use this for add all the rows 
# print x #To print the final result set 
# [All text in bold corresponds to the input and rest corresponds to the output] 
# Sample Input and Output 1:
# +----+-------------+---------+--------------+
# | ID |     Name    | Deposit | Cost_per_day |
# +----+-------------+---------+--------------+
# | 1  |     Food    | 50000.0 |   10000.0    |
# | 2  | Electronics | 85000.0 |   15000.0    |
# | 3  |   Fashion   | 36000.0 |    8000.0    |
# | 4  |   Grooming  | 15000.0 |    5000.0    |
# +----+-------------+---------+--------------+
# Enter the category:
# Food
# +----+-----------+---------+---------------+
# | ID |    Name   | Type_Id |     Vendor    |
# +----+-----------+---------+---------------+
# | 1  | Chocolate |    1    | Foodies Court |
# | 2  |  Lollypop |    1    | Foodies Court |
# +----+-----------+---------+---------------+
# Sample Input and Output 2:
# +----+-------------+---------+--------------+
# | ID |     Name    | Deposit | Cost_per_day |
# +----+-------------+---------+--------------+
# | 1  |     Food    | 50000.0 |   10000.0    |
# | 2  | Electronics | 85000.0 |   15000.0    |
# | 3  |   Fashion   | 36000.0 |    8000.0    |
# | 4  |   Grooming  | 15000.0 |    5000.0    |
# +----+-------------+---------+--------------+
# Enter the category:
# Books
# No such category is present

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

def execute_query(query, params=None):
    try:
        connection = mysql.connector.connect(
            host=dburl,
            database=dbname,
            user=username,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        sys.exit(1)

def display_items():
    query = "SELECT * FROM item"
    result = execute_query(query)
    x = PrettyTable()
    x.field_names = ["ID", "Name", "Deposit", "Cost_per_day"]
    for row in result:
        x.add_row([row[0], row[1], row[2], row[3]])
    print(x)

def display_category(category_name):
    query = """
    SELECT c.id, c.name, c.type_id, c.vendor 
    FROM category c 
    JOIN item i ON c.type_id = i.id
    WHERE i.name = %s
    """
    result = execute_query(query, (category_name,))
    if result:
        x = PrettyTable()
        x.field_names = ["ID", "Name", "Type_Id", "Vendor"]
        for row in result:
            x.add_row([row[0], row[1], row[2], row[3]])
        print(x)
    else:
        print("No such category is present")

def main():
    display_items()
    category_name = input("Enter the category: ").strip()
    display_category(category_name)

if __name__ == "__main__":
    main()
