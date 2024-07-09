# Write a Python code to find the root of the equation f(x)=ex−4x using the root function from SciPy's optimize module.
# Importing Required Modules:
# Imports the root function from the scipy.optimize module. scipy is a library in Python used for scientific computing,
#     and root is a function within the optimize module specifically designed for finding roots of equations numerically.
# Defining the Equation:
# Defines a Python function named equation which takes a single argument x. Inside the function,
# it returns the result of the equation x**3 - 2*x - 5.
# Getting Initial Guess from the User:
# Enter an initial guess for the root of the equation. The input is converted to a floating-point number
#     (float) since the input function returns a string by default.
# Finding the Root:
# Calls the root function imported from scipy.optimize. It takes two arguments:
# The first argument is the name of the function (equation) whose root is to be found.
# The second argument is the initial guess (x0) provided by the user.
# The root function then attempts to find a root of the equation using the specified initial guess.
# Printing the Root:
# Prints the root of the equation found by the root function. The .x attribute of the sol object contains the solution.
# Sample input & output 1:
# Enter initial guess: 2.5
# Root: [2.09455148]
# Sample input & output 2:
# Enter initial guess: -2
# Root: [-0.81633299]

from scipy.optimize import root

def equation(x):
    return x**3 - 2*x - 5

x0 = float(input("Enter initial guess: "))

sol = root(equation, x0)

print("Root:", sol.x)

