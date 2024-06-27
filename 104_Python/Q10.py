'''
Write a Python program that takes a string as input, which contains numbers separated by commas.
Convert the string to a list of numbers and determine whether all the numbers are different from each other.
'''

input_string = input("Enter numbers separated by commas: ")

numbers_str = input_string.split(',')

numbers = [int(num) for num in numbers_str]

seen_numbers = set()

all_different = True

for num in numbers:
    if num in seen_numbers:
        all_different = False
        break
    seen_numbers.add(num)

if all_different:
    print("All numbers are different from each other.")
else:
    print("Not all numbers are different from each other.")