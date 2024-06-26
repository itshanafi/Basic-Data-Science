# Main.py
from Student import Student

def main():
    u_id = int(input("Enter the student id\n"))
    username = input("Enter the student's username\n")
    password = input("Enter the password\n")
    name = input("Enter the name of the student\n")
    address = input("Enter the address\n")
    city = input("Enter the city\n")
    pincode = int(input("Enter the pincode\n"))
    contact_number = int(input("Enter the contact number\n"))
    email = input("Enter the email id\n")

    student = Student(u_id, username, password, name, address, city, pincode, contact_number, email)
    print(student)

if __name__ == "__main__":
    main()

# Student.py
class Student:
    def __init__(self,__id,__username,__password,__name,__address,__city,__pincode,__contact_number,__email):
        self.__id = __id
        self.__username = __username
        self.__password = __password
        self.__name = __name
        self.__address = __address
        self.__city = __city
        self.__pincode = __pincode
        self.__contact_number = __contact_number
        self.__email = __email

# Write a program to display the details of the Student by overriding the __str__() Method.

    def __str__(self):
        return f"id : {self.__id}\nUser Name : {self.__username}\
        \nPassword : {self.__password}\nName : {self.__name}\
        \nAddress : {self.__address}\ncity : {self.__city}\
        \nPincode : {self.__pincode}\nContact Number : {self.__contact_number}\nemail : {self.__email}"