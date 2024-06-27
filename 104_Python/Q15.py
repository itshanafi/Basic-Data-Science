'''
Write a python program which takes a binary number as input and convert the number to decimal. Note: Don't use any builtin functions.
'''

bin_number = input("Enter a binary number: ")

dec_number = 0

for digit in bin_number:
    digit_value = int(digit)
    dec_number = dec_number * 2 + digit_value

print("The decimal representation is:", dec_number)