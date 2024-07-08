# Write a Python program to convert a 1-D array to a 2-D array with m rows and n columns.
# Create the 1-D array using the range function by passing 1 parameter that corresponds to the max value.
# Refer Sample Input and Output for formatting specifications.
# All text in bold corresponds to input and the rest corresponds to output.
# Sample Input and Output :
# Enter the size of 1-D array
# 6
# 1-D Array
# [0 1 2 3 4 5]
# Enter m value
# 3
# Enter n value
# 2
# 2-D Array
# [[0 1]
#  [2 3]
#  [4 5]]

import numpy as np

# Get the size of the 1-D array

size = int(input("Enter the size of 1-D array\n"))

# Create the 1-D array

arr = np.arange(size)

# Print the 1-D array

print("1-D Array")

print(arr)

# Get the values for m and n

m = int(input("Enter m value\n"))

n = int(input("Enter n value\n"))

# Convert the 1-D array to a 2-D array

arr_2d = arr.reshape(m, n)

# Print the 2-D array

print("2-D Array")

print(arr_2d)
