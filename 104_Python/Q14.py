'''
Write a python program which takes a number as input and convert the number to binary. Note: Don't use any builtin functions.
'''

dec_number = int(input("Enter a number: "))

if dec_number == 0:
    bin_number = '0'
else:
    bin_number = ''

while dec_number > 0:
    remainder = dec_number % 2
    bin_number = str(remainder) + bin_number
    dec_number //= 2

print("The binary representation is:", bin_number)