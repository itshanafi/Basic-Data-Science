# Write a program to execute a query to display details student from the 'student' table from the MySQL database.
# In this program, get the details of a table. Write a program to get all the student details.
# Table Schema:
# Note: 
# For display, the result set use PrettyTable 
# For example : 
# from prettytable import PrettyTable.
# x = PrettyTable() 
# x.add_row([....]) #Use this for add all the rows 
# print x #To print the final result set 
# Refer to sample input/output for further details and format of the output.
# Sample Output:
# +----+-----------+------------+
# | Id |    Name   | Department |
# +----+-----------+------------+
# | 1  | Samyuktha |    CSE     |
# | 2  |   Monika  |    EEE     |
# | 3  | Deepshika |    CSE     |
# | 4  |    Sri    |    ECE     |
# +----+-----------+------------+

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
        
        # Executing the query to fetch all student details
        query = "SELECT * FROM student"
        cursor.execute(query)
        
        # Fetching all rows from the executed query
        rows = cursor.fetchall()
        
        # Creating a PrettyTable object
        table = PrettyTable()
        
        # Setting the column names
        table.field_names = ["Id", "Name", "Department"]
        
        # Adding all rows to the PrettyTable object
        for row in rows:
            table.add_row(row)
        
        # Printing the final result set
        print(table)
        
except Error as e:
    print(f"Error: {e}")
    sys.exit(1)
finally:
    # Closing the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
