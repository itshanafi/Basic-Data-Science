import mysql.connector
from mysql.connector import Error
import configparser
from prettytable import PrettyTable

# Read database connection details from configuration file
config = configparser.RawConfigParser()
config.read('mysql.properties')

db_host = config.get('DatabaseSection', 'db.host')
db_schema = config.get('DatabaseSection', 'db.schema')
db_username = config.get('DatabaseSection', 'db.username')
db_password = config.get('DatabaseSection', 'db.password')
db_port = config.getint('DatabaseSection', 'db.port')

# Function to display user table using PrettyTable
def display_user_table(cursor):
    cursor.execute("SELECT * FROM user")
    x = PrettyTable()
    x.field_names = ["ID", "Name", "Mobile", "Username", "Password"]  # Specify the column names explicitly
    x.align = "l"
    for row in cursor.fetchall():
        x.add_row(row)
    print(x)

# Function to delete a user by username
def delete_user_by_username(cursor, username):
    cursor.execute(f"SELECT * FROM user WHERE Username = '{username}'")
    result = cursor.fetchone()
    if result:
        delete_id = result[0]
        cursor.execute(f"DELETE FROM user WHERE ID = {delete_id}")
        print(f"Username {username} with id={delete_id} deleted successfully")
        display_user_table(cursor)
    else:
        print("User not found")
        display_user_table(cursor)

try:
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host=db_host,
        database=db_schema,
        user=db_username,
        password=db_password,
        port=db_port
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        cursor = connection.cursor()

        # Display initial user table
        display_user_table(cursor)

        # Prompt user for username to delete
        username = input("Enter the username to be deleted:\n")

        # Delete user if username exists, otherwise display error
        delete_user_by_username(cursor, username)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
    
