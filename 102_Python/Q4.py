'''
Write a program that takes three numbers as input and prints the largest one.
'''

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

if(num1 >= num2 and num1 >= num3):
  print(f"This {num1} is the largest number")

elif(num2 >= num1 and num1 >= num3):
  print(f"This {num2} is the largest number")

else:
  print(f"This {num3} is the largest number")