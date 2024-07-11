# Write a program to execute a query to insert the hall details in the 'Hall' table using a username of the 'User' table.
# In this program, there are two tables. One is the User and another is Hall. A User will be the owner of a Hall.
# And, the user id is kept in the hall table. So, get the username of the owner, retrieve the name from the user table,
# and get the details of the hall. Then store the hall details in the hall table with the user id. And also,
# display the 'Hall table with owner name.
# Table Schema:
# Note: 
# For display, the result set use PrettyTable 
# For example : 
# from prettytable import PrettyTable.
# x = PrettyTable() 
# x.add_row([....]) #Use this for add all the rows 
# print x #To print the final result set   
# [All Texts in bold corresponds to the input and rest are output]
# Sample Input/Output :
# Enter the user detail in CSV format
# Ball Room,1234567890,15000
# Enter the username:
# jim
# Username seems to be wrong!! Enter the correct username:
# johny
# +-----------------+---------------+---------+-------+
# |       Name      | Mobile Number |   Cost  | Owner |
# +-----------------+---------------+---------+-------+
# |    Party hall   |   9874653201  |  5000.0 |  John |
# |     Ball Room   |   1234567890  | 15000.0 |  John |
# |   Dining Hall   |   9876541230  |  3000.0 | Peter |
# |    Disco Hall   |   9871234560  |  8000.0 |  Adam |
# | Conference Hall |   7891236540  |  7500.0 | Linda |
# |   Meeting Hall  |   8974102365  |  9000.0 |  Tony |
# +-----------------+---------------+---------+-------+

import mysql.connector
import configparser
import sys
from mysql.connector import Error
from prettytable import PrettyTable

# Reading database configuration from 'ysql.properties' file
config = configparser.RawConfigParser()
config.read('mysql.properties')

dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

def get_user_id(username):
    try:
        connection = mysql.connector.connect(host=dburl, database=dbname, user=username, password=password, port=port)
        cursor = connection.cursor()
        
        query = "SELECT user_id FROM User WHERE username = %s"
        values = (username,)
        
        cursor.execute(query, values)
        result = cursor.fetchone()
        
        if result:
            return result[0]
        else:
            return None
        
    except Error as e:
        print(f"Error while getting user id: {e}")
        return None

def insert_hall_details(hall_name, mobile_number, cost, user_id):
    try:
        connection = mysql.connector.connect(host=dburl, database=dbname, user=username, password=password, port=port)
        cursor = connection.cursor()
        
        query = "INSERT INTO Hall (hall_name, mobile_number, cost, user_id) VALUES (%s, %s, %s, %s)"
        values = (hall_name, mobile_number, cost, user_id)
        
        cursor.execute(query, values)
        connection.commit()
        
        print(f"Hall '{hall_name}' inserted successfully.")
        
    except Error as e:
        print(f"Error while inserting hall details: {e}")

def display_hall_details():
    try:
        connection = mysql.connector.connect(host=dburl, database=dbname, user=username, password=password, port=port)
        cursor = connection.cursor()
        
        query = "SELECT h.hall_name, h.mobile_number, h.cost, u.username FROM Hall h JOIN User u ON h.user_id = u.user_id"
        
        cursor.execute(query)
        result = cursor.fetchall()
        
        x = PrettyTable()
        x.field_names = ["Name", "Mobile Number", "Cost", "Owner"]
        
        for row in result:
            x.add_row(row)
        
        print(x)
        
    except Error as e:
        print(f"Error while displaying hall details: {e}")

def main():
    hall_details = input("Enter the hall details in CSV format: ").split(',')
    hall_name = hall_details[0]
    mobile_number = hall_details[1]
    cost = float(hall_details[2])
    
    username = input("Enter the username: ")
    user_id = get_user_id(username)
    
    while user_id is None:
        print("Username seems to be wrong!! Enter the correct username:")
        username = input("Enter the username: ")
        user_id = get_user_id(username)
    
    insert_hall_details(hall_name, mobile_number, cost, user_id)
    display_hall_details()

if __name__ == "__main__":
    main()