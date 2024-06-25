# How to do a program.
# 1. Variables. Assign the values into the variables.
# 2. Input and output function.
# 3. Assignment operator. =
# 4. Arithmetic operator. + - * / % // **
# 5. Comparison operator. == != < > <= =>
# 6. Logical operator. and or not xor
# 7. Decision making.

# Problem 1 inputs
total_liters_1 = float(input("Enter the total liters required for problem 1: "))
desired_concentration_1 = float(input("Enter the desired concentration for problem 1: "))
solution_a_concentration_1 = 25
solution_b_concentration_1 = 50

# Let x be the liters of solution A and y be the liters of solution B
# We have two equations:
# x + y = total_liters_1
# (solution_a_concentration_1 * x + solution_b_concentration_1 * y) / total_liters_1 = desired_concentration_1

# Solving these equations
# From the first equation, y = total_liters_1 - x
# Substituting y in the second equation
# (solution_a_concentration_1 * x + solution_b_concentration_1 * (total_liters_1 - x)) / total_liters_1 = desired_concentration_1
# (solution_a_concentration_1 * x + solution_b_concentration_1 * total_liters_1 - solution_b_concentration_1 * x) / total_liters_1 = desired_concentration_1
# (solution_a_concentration_1 * x + solution_b_concentration_1 * total_liters_1 - solution_b_concentration_1 * x) = desired_concentration_1 * total_liters_1
# (solution_a_concentration_1 * x - solution_b_concentration_1 * x) = desired_concentration_1 * total_liters_1 - solution_b_concentration_1 * total_liters_1
# x * (solution_a_concentration_1 - solution_b_concentration_1) = desired_concentration_1 * total_liters_1 - solution_b_concentration_1 * total_liters_1
# x = (desired_concentration_1 * total_liters_1 - solution_b_concentration_1 * total_liters_1) / (solution_a_concentration_1 - solution_b_concentration_1)
# y = total_liters_1 - x

x_1 = (desired_concentration_1 * total_liters_1 - solution_b_concentration_1 * total_liters_1) / (solution_a_concentration_1 - solution_b_concentration_1)
y_1 = total_liters_1 - x_1

print("\nFor the first problem:")
print(f"Liters of solution A needed: {x_1:.2f}")
if x_1 < 3:
    print("Solution (A) is available, can proceed.")
else:
    print("Solution (A) is not available, please order 1.3 liter now.")
print(f"Liters of solution B needed: {y_1:.2f}")
if y_1 > 3:
    print("Solution (B) is not available, please order 1.3 liter now.")
else:
    print("Solution (B) is available, can proceed.")

# Problem 2 inputs
total_liters_2 = float(input("\nEnter the total liters required for problem 2: "))
desired_concentration_2 = float(input("Enter the desired concentration for problem 2: "))
solution_a_concentration_2 = 15
solution_b_concentration_2 = 40

# Let x be the liters of solution A and y be the liters of solution B
# We have two equations:
# x + y = total_liters_2
# (solution_a_concentration_2 * x + solution_b_concentration_2 * y) / total_liters_2 = desired_concentration_2

# Solving these equations
# From the first equation, y = total_liters_2 - x
# Substituting y in the second equation
# (solution_a_concentration_2 * x + solution_b_concentration_2 * (total_liters_2 - x)) / total_liters_2 = desired_concentration_2
# (solution_a_concentration_2 * x + solution_b_concentration_2 * total_liters_2 - solution_b_concentration_2 * x) / total_liters_2 = desired_concentration_2
# (solution_a_concentration_2 * x + solution_b_concentration_2 * total_liters_2 - solution_b_concentration_2 * x) = desired_concentration_2 * total_liters_2
# (solution_a_concentration_2 * x - solution_b_concentration_2 * x) = desired_concentration_2 * total_liters_2 - solution_b_concentration_2 * total_liters_2
# x * (solution_a_concentration_2 - solution_b_concentration_2) = desired_concentration_2 * total_liters_2 - solution_b_concentration_2 * total_liters_2
# x = (desired_concentration_2 * total_liters_2 - solution_b_concentration_2 * total_liters_2) / (solution_a_concentration_2 - solution_b_concentration_2)
# y = total_liters_2 - x

x_2 = (desired_concentration_2 * total_liters_2 - solution_b_concentration_2 * total_liters_2) / (solution_a_concentration_2 - solution_b_concentration_2)
y_2 = total_liters_2 - x_2

print("\nFor the second problem:")
print(f"Liters of solution A needed: {x_2:.2f}")
if x_2 < 3:
    print("Solution (A) is available, can proceed.")
else:
    print("Solution (A) is not available, please order 1.3 liter now.")
print(f"Liters of solution B needed: {y_2:.2f}")
if y_2 > 3:
    print("Solution (B) is not available, please order 1.3 liter now.")
else:
    print("Solution (B) is available, can proceed.")
