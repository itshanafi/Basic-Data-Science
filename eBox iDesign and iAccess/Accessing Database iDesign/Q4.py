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
        UPDATE user
        SET contact_detail = %s
        WHERE username = %s
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
