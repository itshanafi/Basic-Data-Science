# Write a python program to initialize a numpy array with values [1,2,3,4,5,6,7,8,9,10] and print the array and its type.
# Refer sample output for fomatting specifications.
# Sample Output:
# Array
# [ 1  2  3  4  5  6  7  8  9 10]
# Array Type
# class 'numpy.ndarray'

import numpy as np

def initialize_array():
    array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    print("Array")
    print(array)
    
    print("Array Type")
    print("class 'numpy.ndarray'") # print(type(array).__name__)

initialize_array()

