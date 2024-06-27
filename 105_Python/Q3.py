'''
Write a program that takes two integers from the user and calculates their greatest common divisor (GCD) using the Euclidean algorithm.
'''

def eulidean(A, B):
    while B != 0:
        A, B = B, A % B
    return A

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

print("The GCD of the two numbers is:", eulidean(first_num, second_num))