'''
Get number of items as input and generate that many Armstrong Numbers
'''

num_items = int(input("Enter the number of Armstrong numbers you want to generate: "))

count = 0
number = 1
armstrong_numbers = []

while count < num_items:
    num_digits = len(str(number))
    digit_sum = sum(int(digit) ** num_digits for digit in str(number))

    if digit_sum == number:
        armstrong_numbers.append(number)
        count += 1
    number += 1

print(f"The first {num_items} Armstrong numbers are: {armstrong_numbers}")