# Write a Python program to perform double integration of a function f(x,y) over a specified region using SciPy's dblquad function.
# The user is prompted to enter the function to be integrated in terms of x and y, as well as the lower and upper limits for x and y.
# Then compute the double integral of the function over the specified region and outputs the result along with the error estimate.
# Input Format:
# Enter the function to be integrated in terms of x and y.
# The user is prompted to enter the lower and upper limits for x.
# The user is prompted to enter the lower and upper limits for y.
# Output Format:
# Print the result of the double integration and the error estimate.
# Sample Input and Output:
# Enter the function to be integrated in terms of x and y:
# x**2
# Enter the lower limit for x:
# 0
# Enter the upper limit for x:
# 1
# Enter the lower limit for y:
# 0
# Enter the upper limit for y:
# 2
# Result of dblquad integration: 0.6666666666666667
# Error estimate: 2.2108134835808843e-14

from scipy.integrate import dblquad
import numpy as np

# Define the function to be integrated in terms of x and y
def f(x, y):
    return x**2  # Example function x^2, replace with user input

# Prompt user for input
function_str = input("Enter the function to be integrated in terms of x and y: ")

lower_limit_x = float(input("Enter the lower limit for x: "))
upper_limit_x = float(input("Enter the upper limit for x: "))

lower_limit_y = float(input("Enter the lower limit for y: "))
upper_limit_y = float(input("Enter the upper limit for y: "))

# Define the lambda functions for y limits, since they can depend on x
y_lower_limit_func = lambda x: lower_limit_y
y_upper_limit_func = lambda x: upper_limit_y

# Perform double integration using dblquad
result, error = dblquad(lambda y, x: eval(function_str), lower_limit_x, upper_limit_x, y_lower_limit_func, y_upper_limit_func)

# Print the result and error estimate
print("Result of dblquad integration:", result)
print("Error estimate:", error)

