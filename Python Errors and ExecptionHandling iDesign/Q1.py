# Write a Python program that accepts two numbers as input (say x and y) and finds x/y.
# When the denominator is 0, the program should raise a ZeroDivisionError Exception and print the message shown in the sample output.
# Input Format:
# Input consists of 2 integers
# Output Format:
# Output is either the result or the error message.
# Refer sample output.
# [All text in bold corresponds to input and the rest corresponds to output]
# Sample Input and Output 1:
# Enter number 1
# 6
# Enter number 2
# 3
# 2.0
# Sample Input and Output 2:
# Enter number 1
# 5
# Enter number 2
# 0
# Divide By Zero Error

'''
x = int(input("Enter number 1"))
y = int(input("Enter number 2"))

if y == 0:
    print("Divide By Zero Error")
else:
    print(x / y)
'''

try:
    x = int(input("Enter number 1\n"))
    y = int(input("Enter number 2\n"))

    result = x / y
    print(result)

except ZeroDivisionError:
    print("Divide By Zero Error")
