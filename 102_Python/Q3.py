'''
Write a Python program that takes a year as input and checks whether it is a leap year.
'''

year = int(input("Enter any year to know it is a leap year or not: "))

if(year % 4 == 0):
  print("This is leap year")

else:
  print("Unfortunately, this is not a leap year")