'''
Get number of items as input and generate that many ADAM Numbers
'''

num_items = int(input("Enter the number of Adam numbers you want to generate: "))
count = 0
number = 1
adam_numbers = []

while count < num_items:
    square = number ** 2
    reverse = int(str(number)[::-1])
    reverse_square = int(str(square)[::-1])
    if reverse_square == reverse ** 2:
        adam_numbers.append(number)
        count += 1
    number += 1

print(f"The first {num_items} Adam numbers are: {adam_numbers}")