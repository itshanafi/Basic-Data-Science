'''
Get a number as input and calculate the sum of all numbers from 1 to the given number.
'''

num = int(input("Enter a number: "))

total_sum = 0

for i in range(1, num + 1):
    total_sum += i

print(f"The sum of all numbers from 1 to {num} is: {total_sum}")