'''
Write a python program that takes few numbers as command line argument. Find the average of those numbers.
'''

import sys

arguments = sys.argv[1:]

total_sum = 0
count = 0

for arg in arguments:
    total_sum += int(arg)
    count += 1

average = total_sum / count

print(f"The average of the numbers is: {average}")