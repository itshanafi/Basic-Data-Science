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
'''
import mysql.connector
import configparser
from mysql.connector import Error
from prettytable import PrettyTable

def main():
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
            cursor = conn.cursor(buffered=True)
            
            # Test case 1: Antony,9873216540,Antonie,an@987
            u1 = input('Enter the user detail in CSV format\n')
            d1 = u1.split(",")
            execute_insert_and_display(cursor, conn, d1)
            
    except Error as e:
        print("Error while connecting to MySQL:", e)
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def execute_insert_and_display(cursor, conn, data):
    try:
        # Insert query with placeholders (excluding Id)
        insert_query = "INSERT INTO user (Name, Contactdetail, Username, Password) VALUES (%s, %s, %s, %s)"
        
        # Execute the INSERT query with user input data
        cursor.execute(insert_query, (data[0], data[1], data[2], data[3]))
        conn.commit()
        
        # Select all records query
        select_query = "SELECT * FROM user"
        
        # Execute the SELECT query
        cursor.execute(select_query)
        rows = cursor.fetchall()
        
        # Create a PrettyTable object
        x = PrettyTable()
        x.field_names = ["Id", "Name", "Contact Detail", "Username", "Password"]
        
        # Add rows to the PrettyTable object
        for row in rows:
            x.add_row(row)
        
        # Print the PrettyTable object
        print("\nDisplaying user records after insertion:")
        print(x)
        
    except Error as e:
        print("Error while executing SQL query:", e)

if __name__ == "__main__":
    main()
'''


import mysql.connector,configparser,sys
from mysql.connector import Error
config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host');
dbname = config.get('DatabaseSection', 'db.schema');
username = config.get('DatabaseSection', 'db.username');
password = config.get('DatabaseSection', 'db.password');
port = config.get('DatabaseSection', 'db.port');
from prettytable import PrettyTable
x=PrettyTable()
x.field_names=["Id","Name","Contact Detail","Username","Password"]
try:
    mydb=mysql.connector.connect(host=dburl,port=port,database=dbname,user=username,password=password)
    cursor=mydb.cursor(buffered=True)
    u=input("Enter the user detail in CSV format\n")
    d=u.split(",")
    
    # code here
    insert_query="INSERT INTO user (Name,Contactdetail,Username,Password) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (d[0],d[1],d[2],d[3]))
    mydb.commit()
    
    select_query="SELECT * FROM user"
    cursor.execute(select_query)
    result=cursor.fetchall()

    for row in result:
        x.add_row([row[0],row[1],row[2],row[3],row[4]])
    print (x)
except Error as e:
    print(e)
finally:
    cursor.close()
    mydb.close()



# mysql.properties

[DatabaseSection]
db.host=localhost
db.schema=testdb
db.username=root
db.password=student