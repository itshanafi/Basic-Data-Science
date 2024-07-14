
# Write a program to execute a query to generate a summary of the tables.
# In this program, generate a summary of the tables. Consider a stage event, it has many shows and
# tickets can be booked for each show. When a customer visits to book tickets, the consolidated summary
#     of how many tickets are booked for each show must be displayed.
# Table Name:
# stage_event
# stage_event_show
# ticket_booking
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
# Event 1
# +---------+---------------------+---------------------+---------------+
# | Show Id |    Starting time    |     Ending time     | Ticket booked |
# +---------+---------------------+---------------------+---------------+
# |    1    | 2018-01-01 01:00:00 | 2018-02-01 12:59:59 |       8       |
# +---------+---------------------+---------------------+---------------+
# Event 2
# +---------+---------------------+---------------------+---------------+
# | Show Id |    Starting time    |     Ending time     | Ticket booked |
# +---------+---------------------+---------------------+---------------+
# |    2    | 2018-02-15 12:00:00 | 2018-03-20 11:59:59 |       6       |
# +---------+---------------------+---------------------+---------------+
# Event 3
# +---------+---------------------+---------------------+---------------+
# | Show Id |    Starting time    |     Ending time     | Ticket booked |
# +---------+---------------------+---------------------+---------------+
# |    3    | 2018-03-01 05:00:00 | 2018-04-01 04:59:59 |       6       |
# +---------+---------------------+---------------------+---------------+

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

# Function to generate a summary of the tables
def generate_summary(cursor):
    query = """
    SELECT 
        se.name AS event_name,
        ses.id AS show_id,
        ses.start_time,
        ses.end_time,
        CAST(COALESCE(SUM(tb.no_of_seats), 0) AS UNSIGNED) AS total_seats_booked
    FROM 
        stage_event se
    INNER JOIN 
        stage_event_show ses ON se.id = ses.stage_event_id
    LEFT JOIN 
        ticket_booking tb ON ses.id = tb.stage_event_show_id
    GROUP BY 
        se.name, ses.id, ses.start_time, ses.end_time
    ORDER BY 
        se.name, ses.start_time;
    """
    cursor.execute(query)
    records = cursor.fetchall()
    
    if records:
        current_event = None
        for row in records:
            event_name = row[0]
            if current_event != event_name:
                if current_event is not None:
                    print(table)
                print(event_name)
                table = PrettyTable(["Show Id", "Starting time", "Ending time", "Ticket booked"])
                current_event = event_name
            table.add_row(row[1:])
        print(table)  # Print the last event table
    else:
        print("No records found.")

# Main function
def main():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()

        # Generate and display the summary
        generate_summary(cursor)

        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
