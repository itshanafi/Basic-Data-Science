import mysql.connector
import configparser
from prettytable import PrettyTable

# Read database configuration from properties file
config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

# Connect to MySQL database
try:
    connection = mysql.connector.connect(
        host=dburl,
        database=dbname,
        user=username,
        password=password,
        port=port
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Prompt user for number of halls and their details
        num_halls = int(input("Enter the number of hall details:\n"))
        hall_details = []
        
        for i in range(num_halls):
            hall_detail = input(f"Enter hall {i + 1} detail in CSV format\n").split(',')
            hall_details.append(hall_detail)
        
        # Insert hall details into the 'hall' table
        insert_query = "INSERT INTO hall (hall_name, contact_detail, cost_per_day, organizer) VALUES (%s, %s, %s, %s)"
        for detail in hall_details:
            cursor.execute(insert_query, tuple(detail))
        
        connection.commit()
        
        # Query to display hall details ordered by ascending order of cost_per_day
        select_query = "SELECT * FROM hall ORDER BY cost_per_day ASC"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        
        # Display the result using PrettyTable
        table = PrettyTable()
        table.field_names = ["ID", "Hall name", "Contact detail", "Cost per day", "Organizer"]
        
        for row in rows:
            table.add_row(row)
        
        print(table)
        
except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
