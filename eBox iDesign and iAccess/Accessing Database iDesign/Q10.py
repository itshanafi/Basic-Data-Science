
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
from prettytable import PrettyTable
import configparser

# Function to fetch and display summary of ticket bookings
def generate_ticket_summary():
    try:
        # Read database configuration from properties file
        config = configparser.RawConfigParser()
        config.read('mysql.properties')
        dburl = config.get('DatabaseSection', 'db.host')
        dbname = config.get('DatabaseSection', 'db.schema')
        username = config.get('DatabaseSection', 'db.username')
        password = config.get('DatabaseSection', 'db.password')
        port = config.get('DatabaseSection', 'db.port')

        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host=dburl,
            database=dbname,
            user=username,
            password=password,
            port=port
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # Query to fetch summary of ticket bookings for each show
            query = """
                    SELECT ss.show_id, se.starting_time, se.ending_time, SUM(tb.ticket_count) AS tickets_booked
                    FROM stage_event_show ss
                    JOIN stage_event se ON ss.event_id = se.id
                    LEFT JOIN (
                        SELECT show_id, COUNT(*) AS ticket_count
                        FROM ticket_booking
                        GROUP BY show_id
                    ) tb ON ss.show_id = tb.show_id
                    GROUP BY ss.show_id
                    ORDER BY ss.show_id
                    """
            cursor.execute(query)
            records = cursor.fetchall()

            # Display results using PrettyTable
            if records:
                x = PrettyTable()
                x.field_names = ["Show Id", "Starting time", "Ending time", "Ticket booked"]
                for record in records:
                    x.add_row(record)
                print(x)
            else:
                print("No ticket bookings found.")

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Main program
if __name__ == "__main__":
    try:
        generate_ticket_summary()

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print("Error:", e)
