from prettytable import PrettyTable
import mysql.connector
import configparser
import sys
from mysql.connector import Error

# Read database configuration from the properties file
config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

# Function to connect to the database
def connect_to_db():
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
        print(f"Error: {e}")
        sys.exit(1)

# Function to alter the id column to auto-increment
def alter_id_column(connection):
    try:
        cursor = connection.cursor()
        alter_query = "ALTER TABLE hall MODIFY id BIGINT(20) NOT NULL AUTO_INCREMENT"
        cursor.execute(alter_query)
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
        connection.rollback()

# Function to insert hall details into the database
def insert_hall_details(connection, hall_details):
    try:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO hall (hall_name, contact_detail, cost_per_day, organizer)
            VALUES (%s, %s, %s, %s)
        """
        cursor.executemany(insert_query, hall_details)
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
        connection.rollback()

# Function to display hall details ordered by cost_per_day
def display_hall_details(connection):
    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM hall ORDER BY cost_per_day ASC"
        cursor.execute(select_query)
        rows = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["ID", "Hall name", "Contact detail", "Cost per day", "Organizer"]

        for row in rows:
            table.add_row(row)
        
        print(table)
    except Error as e:
        print(f"Error: {e}")

# Main function
def main():
    connection = connect_to_db()
    
    # Alter the id column to be auto-increment
    alter_id_column(connection)
    
    print("Enter the number of hall details:")
    num_halls = int(input())
    hall_details = []
    for i in range(num_halls):
        print(f"Enter hall {i+1} detail in CSV format")
        hall_detail = input().split(',')
        if len(hall_detail) == 4:
            hall_details.append(tuple(hall_detail))
        else:
            print("Invalid input format. Please enter exactly four values separated by commas.")
    
    insert_hall_details(connection, hall_details)
    display_hall_details(connection)
    
    if connection.is_connected():
        connection.close()

if __name__ == "__main__":
    main()
