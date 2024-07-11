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
from prettytable import PrettyTable

# Function to connect to MySQL database
import mysql.connector
from prettytable import PrettyTable
import configparser

# Function to fetch stall details for a given exhibition name
def fetch_stalls_for_exhibition(exhibition_name):
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

            # Prepare SQL query to fetch stalls for the given exhibition name
            query = """
                    SELECT s.stall_name, s.detail, s.owner_name
                    FROM stall s
                    JOIN exhibition e ON s.exhibition_id = e.id
                    WHERE e.name = %s
                    """
            cursor.execute(query, (exhibition_name,))
            records = cursor.fetchall()

            # Display results using PrettyTable
            if records:
                x = PrettyTable()
                x.field_names = ["Stall Name", "Detail", "Owner Name"]
                for record in records:
                    x.add_row(record)
                print(x)
            else:
                print("No stalls found for the exhibition:", exhibition_name)

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Main program
if __name__ == "__main__":
    try:
        while True:
            exhibition_name = input("Enter the exhibition name: ").strip()
            if exhibition_name.lower().startswith("exhibition"):
                fetch_stalls_for_exhibition(exhibition_name)
                break
            else:
                print("Enter the correct exhibition name:")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print("Error:", e)
