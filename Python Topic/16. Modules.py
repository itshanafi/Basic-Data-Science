# creating a function of arithmetic to create a modules
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y
    
# creating a module
import mymath   # import Modules(the name of the file)
print(mymath.add(10, 5)) # Output: 15
print(mymath.subtract(10, 5)) # Output: 5
print(mymath.multiply(10, 5)) # Output: 50
print(mymath.divide(10, 5)) # Output: 2.0

# creating a module with alias
import mymath as mm
print(mm.add(10, 5)) # Output: 15

# creating a module from a specific function
from mymath import add
print(add(10, 5)) # Output: 15

# creating a module from all functions
from mymath import *
print(add(10, 5)) # Output: 15
print(subtract(10, 5)) # Output: 5

# creating a module with dir() function
import mymath
print(dir(mymath)) # Output: ['__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__',
# '__spec__', 'add', 'divide', 'multiply', 'subtract']
# creating a module with help() function

import mymath
help(mymath) # Output: Help on module mymath:
# NAME
#     mymath
# FILE
#     /path/to/mymath.py
# MODULE DOCS
#     http://docs.python.org/3/library/mymath
#     (created by the `help` function)
# FUNCTION
#     add(x, y)
#         return x + y
#     divide(x, y)
#         return x / y
#     multiply(x, y)
#         return x * y
#     subtract(x, y)
#         return x - y
# creating a module with reload() function

import mymath
import importlib
importlib.reload(mymath) # Output: <module 'mymath' from '/path to/mymath.py'>
# creating a module with __name__ variable

import mymath
print(mymath.__name__) # Output: mymath

# creating a module with __package__ variable
import mymath
print(mymath.__package__) # Output: None
