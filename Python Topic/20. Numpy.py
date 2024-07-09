quantities = [10, 20, 30, 40, 50]
new_quantities = [5, 15, 25, 35, 45]

total_quantities = zip(quantities, new_quantities)
print(total_quantities)
print(list(total_quantities))

total_quantities = [x + y for x, y in zip(quantities, new_quantities)]
print(total_quantities)

import timeit
import numpy as np


size = 100000
a = range(0, size)
b = range(0, size)
numpya = np.arange(0, size)
numpyb = np.arange(0, size)

# Using timeit to measure execution time
def addition_time():
    c = [x + y for x, y in zip(a, b)]

def add_time():
    d = numpya + numpyb

# Measure the execution time
execution_time = timeit.timeit(addition_time, number=10)
exute_time = timeit.timeit(add_time, number=10)
print(f"Execution time: {execution_time} seconds")
print(f"Execution time: {exute_time} seconds")

# https://github.com/thajegan76