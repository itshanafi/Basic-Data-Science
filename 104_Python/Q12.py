'''
Write a Python program to get 2 positive numbers as input and multiply them without using the '*' operator.
'''

num1 = int(input("Enter the first positive number: "))
num2 = int(input("Enter the second positive number: "))

result = 0

for i in range(num2):
    result += num1

print(f"The product of {num1} and {num2} is: {result}")