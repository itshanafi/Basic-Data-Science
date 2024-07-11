# Write a program to execute a query to display the details of an event from the ' event '
# table in the MySQL database and obtain details from the user to update and display the details of the event table.
# In this program, display the user table first and prompt the user to provide a userid.
# If the userid is present in the User table, get the start date and end date to be updated and update it in the User table.
# Otherwise, Display an error message as ‘Id not found’ and terminate the program.
# Table Schema:
# If the user enters an Id , which is not in the table, then print ‘Id not found’
# Note: 
# For display, the result set use PrettyTable
# For example : 
# from prettytable import PrettyTable.
# x = PrettyTable() 
# x.add_row([....]) #Use this for add all the rows 
# print x #To print the final result set  
# [All text in bold corresponds to the input and rest corresponds to the output]
# Sample Input/Output:
# +----+------------+---------------------+---------------------+-----------+
# | ID | Event name |      Start date     |       End date      | Organizer |
# +----+------------+---------------------+---------------------+-----------+
# | 1  |  Event_1   | 2018-01-01 12:00:00 | 2018-02-01 12:00:00 |    John   |
# | 2  |  Event_2   | 2018-02-15 18:00:00 | 2018-03-20 15:00:00 |   Peter   |
# | 3  |  Event_3   | 2018-03-01 15:00:00 | 2018-04-01 00:00:00 |    Mark   |
# | 4  |  Event_4   | 2018-03-01 12:00:00 | 2018-03-10 18:00:00 |  Stephen  |
# | 5  |  Event_5   | 2018-11-11 00:00:00 | 2018-12-01 12:00:00 |  Charles  |
# +----+------------+---------------------+---------------------+-----------+

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
        
        # Executing the query to fetch all event details
        query = "SELECT * FROM event"
        cursor.execute(query)
        
        # Fetching all rows from the executed query
        rows = cursor.fetchall()
        
        # Creating a PrettyTable object
        table = PrettyTable()
        
        # Setting the column names
        table.field_names = ["ID", "Event name", "Start date", "End date", "Organizer"]
        
        # Adding all rows to the PrettyTable object
        for row in rows:
            table.add_row(row)
        
        # Printing the final result set
        print(table)
        
        # Prompting the user for an event ID to update
        print("Enter the id of the event to be updated")
        event_id = input()
        
        # Checking if the entered ID exists in the table
        cursor.execute("SELECT COUNT(*) FROM event WHERE ID = %s", (event_id,))
        count = cursor.fetchone()[0]
        
        if count == 0:
            print("Id not found")
            sys.exit(1)
        
        # Getting the new start and end dates from the user
        print("Enter the start and end date")
        start_date = input()
        end_date = input()
        
        # Updating the event with the new dates
        update_query = "UPDATE event SET start_date = %s, end_date = %s WHERE ID = %s"
        cursor.execute(update_query, (start_date, end_date, event_id))
        connection.commit()
        
        # Re-fetching and displaying the updated event table
        cursor.execute(query)
        rows = cursor.fetchall()
        
        table.clear_rows()
        for row in rows:
            table.add_row(row)
        
        print(table)
        
except Error as e:
    print(f"Error: {e}")
    sys.exit(1)
finally:
    # Closing the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
