# Write a program to execute a SELECT query to display all the records from ‘item’ table.
# In this program, the SELECT statement is used to retrieve the records from the database based on the client's need.
# The retrieved data will be stored in a Result and this Result is used to display those selected records.
# Here, use a SELECT statement to display the records from the ‘item’ table.
# Table Schema:
# Note: 
# For display the result set use PrettyTable 
# For example : 
# from prettytable import PrettyTable.
# x = PrettyTable() 
# x.add_row([....]) #Use this for add all the rows 
# print x #To print the final result set   
# [All text in bold corresponds to the input and rest corresponds to the output]
# Sample Input and Output:
# +----+-------------+---------+--------------+
# | ID |     Name    | Deposit | Cost per day |
# +----+-------------+---------+--------------+
# | 1  |     Food    | 50000.0 |   10000.0    |
# | 2  | Electronics | 85000.0 |   15000.0    |
# | 3  |   Fashion   | 36000.0 |    8000.0    |
# | 4  |   Grooming  | 15000.0 |    5000.0    |
# | 5  |    Books    | 20000.0 |    7500.0    |
# +----+-------------+---------+--------------+

# Main.py

import mysql.connector
import configparser
import sys
from mysql.connector import Error
from prettytable import PrettyTable

def main():
    # Read MySQL database configuration from properties file
    config = configparser.RawConfigParser()
    config.read('mysql.properties')

    dburl = config.get('DatabaseSection', 'db.host')
    dbname = config.get('DatabaseSection', 'db.schema')
    username = config.get('DatabaseSection', 'db.username')
    password = config.get('DatabaseSection', 'db.password')
    port = config.get('DatabaseSection', 'db.port')

    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host=dburl,
            database=dbname,
            user=username,
            password=password,
            port=port
        )
        
        if conn.is_connected():            
            cursor = conn.cursor()
            sql_query = "SELECT * FROM item"
            
            try:
                # Execute the SQL query
                cursor.execute(sql_query)
                
                # Fetch all the rows
                rows = cursor.fetchall()
                
                # Get column names
                column_names = [desc[0].replace('_',(' ')).capitalize() for desc in cursor.description]
                
                # Create a PrettyTable object
                x = PrettyTable()
                
                # Set the column names
                x.field_names = column_names
                
                # Add rows to the PrettyTable object
                for row in rows:
                    x.add_row(row)
                
                # Print the PrettyTable object
                print(x)
            
            except Error as e:
                print("Error while executing the SQL query:", e)
            
            finally:
                cursor.close()
                conn.close()

    except Error as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()


# mysql.properties

[DatabaseSection]
db.host=localhost
db.schema=testdb
db.username=root
db.password=student
