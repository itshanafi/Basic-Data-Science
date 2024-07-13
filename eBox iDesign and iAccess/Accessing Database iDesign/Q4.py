# Write a program to execute a query to display the details of a user from the 'user' table in a MySql database
# and also update contact details and display the details for that user.
# In this program, display the user table first and prompt the user to provide a username.
# If the username is present in the user table, get the contact details to be updated and update it in the user table.
# Otherwise, Display an error message.
# Table Schema:
# Note: 
# For display, the result set use PrettyTable 
# For example : 
# from prettytable import PrettyTable.
# x = PrettyTable() 
# x.add_row([....]) #Use this for add all the rows 
# print x #To print the final result set  
# [All text in bold corresponds to the input and rest corresponds to the output]
# Sample Input and Output 1:
# +----+-------+----------------+-----------+----------+

# | Id |  Name | Contact Detail |  Username | Password |

# +----+-------+----------------+-----------+----------+

# | 1  |  John |   9876543210    |   johny   |  12345   |

# | 2  | Peter |   9873216540   |  peterey  |  pet123  |

# | 3  |  Adam |   9871236504   |  adamanta |  ad@123  |

# | 4  | Linda |   8794561320   | lindahere |   abcd   |

# | 5  |  Tony |   7894561230   |   tonii   |  abc123  |

# +----+-------+----------------+-----------+----------+
# Enter the username:
# John
# +----+------+----------------+----------+----------+

# | Id | Name | Contact Detail | Username | Password |

# +----+------+----------------+----------+----------+

# | 1  | John |   9876543210   |  johny   |  12345   |

# +----+------+----------------+----------+----------+
# Enter the mobile number to be updated:
# 9621675431
# +----+------+----------------+----------+----------+

# | Id | Name | Contact Detail | Username | Password |

# +----+------+----------------+----------+----------+

# | 1  | John |   9621675431   |  johny   |  12345   |

# +----+------+----------------+----------+----------+
# Sample Input and Output 2:

# +----+-------+----------------+-----------+----------+

# | Id |  Name | Contact Detail |  Username | Password |

# +----+-------+----------------+-----------+----------+

# | 1  |  John |   9620685431   |   johny   |  12345   |

# | 2  | Peter |   9873216540   |  peterey  |  pet123  |

# | 3  |  Adam |   9871236504   |  adamanta |  ad@123  |

# | 4  | Linda |   8794561320   | lindahere |   abcd   |

# | 5  |  Tony |   7894561230   |   tonii   |  abc123  |

# +----+-------+----------------+-----------+----------+
# Enter the username:
# admin
# No such user is present


import mysql.connector
from prettytable import PrettyTable
import configparser

# Reading MySQL database properties from 'mysql.properties'
config = configparser.RawConfigParser()
config.read('mysql.properties')

dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')

# Establishing connection to MySQL database
conn = mysql.connector.connect(
    host=dburl,
    database=dbname,
    user=username,
    password=password
)

cursor = conn.cursor()

# Function to fetch all users from the 'user' table
def fetch_all_users():
    cursor.execute('SELECT Id, name, contactDetail, username, password FROM user')
    return cursor.fetchall()

# Function to display users using PrettyTable
def display_users(rows):
    x = PrettyTable()
    x.field_names = ["Id", "Name", "Contact Detail", "Username", "Password"]
    for row in rows:
        x.add_row(row)
    print(x)

# Function to update contact detail for a user
def update_contact_detail(username, new_contact_detail):
    update_query = '''
        # UPDATE user
        # SET contact_detail = %s
        # WHERE username = %s
    '''
    cursor.execute(update_query, (new_contact_detail, username))
    conn.commit()

# Main function to run the program
def main():
    # Display current users
    current_users = fetch_all_users()
    print("\nCurrent Users Table:")
    display_users(current_users)
    
    # Prompt user for name input
    print("\nEnter the name:")
    name = input().strip()
    
    # Find the user by name
    user_found = False
    for user in current_users:
        if user[1] == name:  # Checking against Name column
            user_found = True
            username = user[3]  # Get username to update contact detail
            break
    
    if not user_found:
        print("\nNo such user is present")
    else:
        # Prompt for new contact detail
        print("\nEnter the mobile number to be updated:")
        new_contact_detail = input().strip()
        
        # Update contact detail in the user table
        update_contact_detail(username, new_contact_detail)
        
        # Display updated user information
        updated_users = fetch_all_users()
        print("\nUpdated Users Table:")
        display_users(updated_users)

if __name__ == "__main__":
    main()

# Closing database connection
cursor.close()
conn.close()


#################################################################################################

import mysql.connector
import configparser
from mysql.connector import Error
from prettytable import PrettyTable

# Read database configuration from properties file
config = configparser.RawConfigParser()
config.read('mysql.properties')

dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

# Initialize PrettyTable
x = PrettyTable()
x.field_names = ["Id", "Name", "Contact Detail", "Username", "Password"]

try:
    # Connect to the database
    mydb = mysql.connector.connect(host=dburl, port=port, database=dbname, user=username, password=password)
    cursor = mydb.cursor(buffered=True)
    
    # Display user table
    select_query = "SELECT * FROM user"
    cursor.execute(select_query)
    result = cursor.fetchall()

    print("+----+--------+----------------+-----------+----------+")
    for row in result:
        print(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |")
    print("+----+--------+----------------+-----------+----------+")
    
    # Prompt user for username to update contact details
    print("Enter the username:")
    username_input = input().strip()
    
    # Check if the username exists in the user table
    select_user_query = "SELECT * FROM user WHERE name = %s"
    cursor.execute(select_user_query, (username_input,))
    user = cursor.fetchone()
    
    if user:
        print("Enter the mobile number to be updated:")
        new_contact_detail = input().strip()
        
        # Update contact details for the user
        update_query = "UPDATE user SET contactDetail = %s WHERE name = %s"
        cursor.execute(update_query, (new_contact_detail, username_input))
        mydb.commit()
        
        # Display updated user details
        select_updated_query = "SELECT * FROM user WHERE name = %s"
        cursor.execute(select_updated_query, (username_input,))
        updated_user = cursor.fetchone()

        print("+----+--------+----------------+-----------+----------+")
        print(f"| {updated_user[0]} | {updated_user[1]} | {updated_user[2]} | {updated_user[3]} | {updated_user[4]} |")
        print("+----+--------+----------------+-----------+----------+")
        
    else:
        print("No such user is present.")
    
except Error as e:
    print(f"Error: {e}")

finally:    
    if cursor:
        cursor.close()
    if mydb:
        mydb.close()


    