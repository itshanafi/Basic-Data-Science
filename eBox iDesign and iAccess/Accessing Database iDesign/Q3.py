# Write a program to execute an INSERT query to accept run-time parameters and display all the records from the 'user' table.
# Table Schema:
# Table Name: 'user'
# Note: For display, the result set use PrettyTable 
# For example : 
# from prettytable import PrettyTable.
# x = PrettyTable() 
# x.add_row([....]) #Use this for add all the rows 
# print x #To print the final result set
# [All text in bold corresponds to the input and rest corresponds to the output]
# Sample Input/Output:
# Enter the user detail in CSV format
# Antony,9873216540,Antonie,an@987
# +----+--------+----------------+-----------+----------+
# | Id |  Name  | Contact Detail |  Username | Password |
# +----+--------+----------------+-----------+----------+
# | 1  |  John  |   9876543210   |   johny   |  12345   |
# | 2  | Peter  |   9873216540   |  peterey  |  pet123  |
# | 3  |  Adam  |   9871236504   |  adamanta |  ad@123  |
# | 4  | Linda  |   8794561320   | lindahere |   abcd   |
# | 5  |  Tony  |   7894561230   |   tonii   |  abc123  |
# | 6  | Antony |   9873216540   |  Antonie  |  an@987  |
# +----+--------+----------------+-----------+----------+

# Main.py
import mysql.connector
import configparser
from mysql.connector import Error
from prettytable import PrettyTable

# Load database configuration from properties file
config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')

# Define PrettyTable structure
x = PrettyTable()
x.field_names = ["Id", "Name", "Contact Detail", "Username", "Password"]

try:
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        host=dburl,
        database=dbname,
        user=username,
        password=password
    )
    cursor = mydb.cursor(buffered=True)

    # Alter the 'user' table to set 'id' as AUTO_INCREMENT
    alter_query = "ALTER TABLE user MODIFY id BIGINT AUTO_INCREMENT"
    cursor.execute(alter_query)
    mydb.commit()

    # Accept user input in CSV format
    print("Enter the user detail in CSV format")
    u = input()
    d = u.split(",")

    # Execute the INSERT query
    insert_query = "INSERT INTO user (Name,Contactdetail,Username,Password) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (d[0], d[1], d[2], d[3]))
    mydb.commit()

    # Fetch all records from the 'user' table
    select_query = "SELECT * FROM user"
    cursor.execute(select_query)
    result = cursor.fetchall()

    # Add rows to PrettyTable
    for row in result:
        x.add_row([row[0], row[1], row[2], row[3], row[4]])

    # Print the final result set
    print(x)

except Error as e:
    print(e)

finally:
    if cursor is not None:
        cursor.close()
    if mydb is not None:
        mydb.close()
