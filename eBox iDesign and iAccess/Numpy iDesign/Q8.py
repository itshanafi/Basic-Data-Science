# Write a Python program to perform the following Set Operations on Numpy Arrays.
# 1) Union of A and B
# 2) Intersection on A and B
# 3) A difference B
# Get the array size and elements as input from the user. Consider 1-D float array.
# Refer Sample Input and Output for formatting specifications.
# All text in bold corresponds to input and the rest corresponds to output.
# Sample Input and Output :
# Enter the size of 1st array
# 2
# Enter the elements of first array
# 1
# 2
# Enter the size of 2nd array
# 2
# Enter the elements of second array
# 2
# 3
# Union Array
# [1. 2. 3.]
# Intersection Array
# [2.]
# Difference Array
# [1.]

import numpy as np

size_array1 = int(input("Enter the size of 1st array\n"))
print("Enter the elements of first array")
array1 = np.array([float(input()) for _ in range(size_array1)])

size_array2 = int(input("Enter the size of 2nd array\n"))
print("Enter the elements of second array")
array2 = np.array([float(input()) for _ in range(size_array2)])

union_array = np.union1d(array1, array2)

intersection_array = np.intersect1d(array1, array2)

difference_array = np.setdiff1d(array1, array2)

print("Union Array")

print(union_array)

print("Intersection Array")

print(intersection_array)

print("Difference Array")

print(difference_array)