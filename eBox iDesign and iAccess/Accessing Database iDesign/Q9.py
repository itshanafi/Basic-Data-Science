# Write a program to execute a query to display details stalls from the 'stall' table from the
# MySQL database using the exhibition name from the 'exhibition' table.
# In this program, get the details of a table. There are many exhibitions in n and each exhibition has booked many stalls.
# So write a program to get all the stalls booked for the given exhibition.
# Table Schema:
# Note: 
# For display, the result set use PrettyTable 
# For example : 
# from prettytable import PrettyTable.
# x = PrettyTable() 
# x.add_row([....]) #Use this for add all the rows 
# print x #To print the final result set 
# Refer to sample input/output for further details and format of the output.
# [All Texts in bold corresponds to the input and rest are output]
# Sample Input/Output 1:
# Enter the exhibition name:
# Exhibition
# Enter the correct exhibition name:
# Exhibition 10
# Enter the correct exhibition name:
# Exhibition 1
# +------------------+-----------------+------------+
# |    Stall Name    |      Detail     | Owner Name |
# +------------------+-----------------+------------+
# | Chocolate stall  |  chocolate shop |    John    |
# | HiFi electronics |   mobile shop   |    Adam    |
# |   Snack seeker   | shop for snacks |    Mark    |
# +------------------+-----------------+------------+

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

# Function to check if an exhibition exists
def exhibition_exists(cursor, exhibition_name):
    query = "SELECT COUNT(*) FROM exhibition WHERE name = %s"
    cursor.execute(query, (exhibition_name,))
    return cursor.fetchone()[0] > 0

# Function to fetch and display stalls for a given exhibition name
def display_stalls_for_exhibition(cursor, exhibition_name):
    query = """
    SELECT s.stall_name, s.detail, s.owner_name
    FROM stall s
    INNER JOIN exhibition e ON s.exhibition_id = e.id
    WHERE e.name = %s
    """
    cursor.execute(query, (exhibition_name,))
    records = cursor.fetchall()
    
    if records:
        table = PrettyTable(["Stall Name", "Detail", "Owner Name"])
        for row in records:
            table.add_row(row)
        print(table)
    else:
        print(f"No stalls found for exhibition: {exhibition_name}")

# Main function
def main():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()

        print("Enter the exhibition name:")
        while True:
            
            exhibition_name = input()
            if exhibition_exists(cursor, exhibition_name):
                break
            print("Enter the correct exhibition name:")

        display_stalls_for_exhibition(cursor, exhibition_name)

        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
