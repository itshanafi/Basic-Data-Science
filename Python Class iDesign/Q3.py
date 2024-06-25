# Create a class named Address with the following private_attributes
# __street
# __city
# __state
# Include a constructor
# __init__(self, street, city, state)
#  Include a method
# __str__(self)
# This method returns a string corresponding to Address details in the format specified
# in the sample output.
# Create a class named Person with the following private_attributes
# __name
# __age
# __address (of type Address)
# Include a constructor
# __init__(self, name, age, address)
# Include a method
# __str__(self)
# This method returns a string corresponding to Person details in the format specified
# in the sample output.
# Create objects of the above classes and test them.
# Input and Output Format:
# Refer Sample Input and Output for formatting specifications.
# Sample Input and Output 1:
# [All text in bold corresponds to input and the rest corresponds to output]
# Enter name
# Mahirl
# Enter age
# 10
# Enter address
# Enter street
# LMC Street
# Enter city
# Salem
# Enter state
# Tamilnadu
# Person Details
# Mahirl is a person who is 10 years old and lives in the following address : LMC Street , Salem , Tamilnadu

# Main.py
from Person import Person
from Address import Address

person_name = input("Enter name\n")
person_age = input("Enter age\n")
print("Enter address")
street = input("Enter street\n")
city = input("Enter city\n")
state = input("Enter state\n")
person_address = Address(street,city,state)
person = Person(person_name, person_age,person_address)
print("Person Details")
print(person)

# Address.py
class Address:
	
	def __init__(self,street, city, state):
		self.__street = street
		self.__city = city
		self.__state = state
	
	def __str__(self):
		return self.__street + " , " + self.__city + " , " + self.__state

# Person.py
from Address import Address
class Person:
	
	def __init__(self,name, age, address):
		self.__name = name
		self.__age = age
		self.__address = address
	
	def __str__(self):
		return self.__name + " is a person who is " + self.__age + " years old and lives in the following address : " + str(self.__address)
