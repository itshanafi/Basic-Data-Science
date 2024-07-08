# Write a Python code to check duplicate user details. There can be only one user with a specific mobile number.
# If two users exist with the same mobile number they are duplicate. Check whether user information is the same or not by overriding
# the equals method.
# Create a User class with the following attributes 
# Attributes
# Datatype
# name str
# username str
# password str
# mobile_number int
# Use __init__() constructor to initialize the variables with respect to class.
# Override __eq__() method that compares mobile_number of the two objects.
# Input format :
# Input consists of 2 user’s details, which contains (name, username, password, mobile_number).
# Output format :
# The output is a string value, denoting whether the users were same or not by comparing the mobile number of the user.
# [All Texts in bold corresponds to the input and rest are output] 
# Sample Input and Output - 1:
# Enter the details of User 1
# Name :
# Meena
# Username :
# Meena2020
# Password :
# Basic
# Mobile Number :
# 1234567890
# Enter the details of User 2
# Name :
# Meena
# Username :
# Meena1010
# Password :
# Probob
# Mobile Number :
# 0987654321
# User 1 and User 2 are not equal

# Sample Input and Output - 2:
# Enter the details of User 1
# Name :
# Vasu
# Username :
# Va450
# Password :
# particles
# Mobile Number :
# 9894098490
# Enter the details of User 2
# Name :
# Vasu
# Username :
# Vasavi
# Password :
# 500
# Mobile Number :
# 9894098490
# User 1 and User 2 are equal

# Main.py
from User import User

def get_user_details(user_number):
    print(f"Enter the details of User {user_number}")
    name = input("Name :\n")
    username = input("Username :\n")
    password = input("Password :\n")
    mobile_number = int(input("Mobile Number :\n"))
    return User(name, username, password, mobile_number)

# Main function to compare two users
def main():
    user1 = get_user_details(1)
    user2 = get_user_details(2)

    if user1 == user2:
        print(f"User 1 and User 2 are equal")
    else:
        print(f"User 1 and User 2 are not equal")

if __name__ == "__main__":
    main()

# User.py
class User:
    def __init__(self,name,username,password,mobile_number):
        self.name = name
        self.username = username
        self.password = password
        self.mobile_number = mobile_number

    def __eq__(self, other):
        if isinstance(other, User):
            return self.mobile_number == other.mobile_number
        return False