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
import configparser
from mysql.connector import Error

config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

def display_user_details(username):
    try:
        conn = mysql.connector.connect(host=dburl, database=dbname, user=username, password=password)
        cursor = conn.cursor()
        query = "SELECT * FROM user WHERE username=%s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if user:
            print(f"User Details for {username}:")
            print(f"+----+------+----------------+----------+----------+")
            print(f"| ID | Name | Contact Detail | Username | Password |")
            print(f"+----+------+----------------+----------+----------+")
            print(f"| {user[0]}  | {user[1]} |   {user[2]}   |  {user[3]}   |  {user[4]}   |")
            print(f"+----+------+----------------+----------+----------+")
            return True
        else:
            print(f"No such user is present: {username}")
            return False
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return False
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def main():
    username_input = input("Enter the username: ")
    if display_user_details(username_input):
        contact_detail = input("Enter the mobile number to be updated: ")
        try:
            conn = mysql.connector.connect(host=dburl, database=dbname, user=username, password=password)
            cursor = conn.cursor()
            query = "UPDATE user SET ContactDetail=%s WHERE username=%s"
            cursor.execute(query, (contact_detail, username_input))
            conn.commit()
            print(f"Contact details updated for {username_input}:")
            print(f"+----+------+----------------+----------+----------+")
            print(f"| ID | Name | Contact Detail | Username | Password |")
            print(f"+----+------+----------------+----------+----------+")
            print(f"| {cursor.lastrowid}  | {username_input} |   {contact_detail}   |  {username_input}   |  (hidden)   |")
            print(f"+----+------+----------------+----------+----------+")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    main()
