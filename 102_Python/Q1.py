'''
Write a Python program that takes an integer as input and checks whether it is even or odd.
'''

number = int(input("Please enter a number to know it is even or odd: "))

if(number % 2 == 0):
  print(f"This number, {number} is a even number")

else:
  print(f"This number, {number} is a odd number")