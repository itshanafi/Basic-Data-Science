# Vicky's father wants to create the whatsApp account. But again and again Invalid Password error comes.
# So Vicky helps his father to create a account. During account creation he has enter the username and password,
# in which the password should be contain atleast one lowercase letter, one upper case letter and a number, otherwise exception occured.
# So write a program to check the password is valid or invalid.
# Note:
# Conditions for a valid password: 
# Password should contain atleast one lowercase letter, one upper case letter and a number. 
# Use exception handling mechanisms to handle these exceptions 
# Input and Output Format: 
# Refer sample input and output for formatting specifications. 
# All text in bold corresponds to input and the rest corresponds to output. 
# Sample Input and Output 1 : 
# Enter the username
# Vikram
# Enter the password 
# 1samudrA
# Employee Username: Vikram
# Password: 1samudrA
# Sample Input and Output 2 : 
# Enter the username 
# Rashmi
# Enter the password 
# hawai
# CustomException: Invalid Password Exception

'''
def main():
    try:
        username = input("Enter the username:")
        password = input("Enter the password:")

        if len(password) < 8:
            raise Exception("Invalid Password Exception")
        elif not any(char.islower() for char in password):
            raise Exception("Invalid Password Exception")
        elif not any(char.isupper() for char in password):
            raise Exception("Invalid Password Exception")
        elif not any(char.isdigit() for char in password):
            raise Exception("Invalid Password Exception")
        else:
            print("Employee Username:",username)
            print("Password:",password)

    except Exception as e:
        print("CustomException:",e)

if __name__ == '__main__':
    main()
'''
'''
class CustomException(Exception):
    pass
def main():
    try:
        username = input("Enter the username:")
        password = input("Enter the password:")
        if len(password) < 8:
            raise CustomException("Invalid Password Exception")
        elif not any(char.islower() for char in password):
            raise CustomException("Invalid Password Exception")
        elif not any(char.isupper() for char in password):
            raise CustomException("Invalid Password Exception")
        elif not any(char.isdigit() for char in password):
            raise CustomException("Invalid Password Exception")
        else:
            print("Employee Username:",username)
            print("Password:",password)
            
    except CustomException as e:
        print("CustomException:",e)

if __name__ == '__main__':
    main()
'''


class CustomException(Exception):
    pass

def check_password(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if has_lower and has_upper and has_digit:
        print("Password is valid.")
    else:
        raise CustomException("CustomException: Invalid Password Exception")

if __name__ == "__main__":
    try:
        username = input("Enter the username\n")
        password = input("Enter the password\n")
        
        check_password(password)
        
        print(f"Employee Username: {username}")
        print(f"Password: {password}")
        
    except CustomException as e:
        print(e)
