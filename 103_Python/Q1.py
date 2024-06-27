'''
A laboratory technician always needs to prepare various solutions.
Coming Sunday, he has to create a 20-liter solution that is 35% salt by mixing two available solutions.
One solution (A) is 25% salt, and the other solution (B) is 50% salt.
How many liters of each solution are required to achieve the desired concentration?
Coming Monday, he has to create an 8-liter solution that is 25% sugar by mixing two available solutions.
One solution (A) is 15% sugar, and the other solution (B) is 40% sugar. How many liters of each solution are
required to achieve the desired concentration?
Write a simple, generic Python program to assist the laboratory technician. The program must take all these numbers
(20 liters, 35, 25, 50) as input and calculate the required liters of each solution and print them.
Please note that the same program must work for the second problem as well (8 liters, 25, 15, 40).
The maximum stock for solution (A) and solution (B) is always 3 liter only. After calculating/printing
the required quantity of A and B, throw proper message. For example, required quantity of solution (A) is less than 3 liter say
"Solution (A) is available can proceed". If required quantity of solution (B) is greater than 3 liter say "Solution (B) is not available,
please order 1.3 liter now".
'''

# Sunday
total_liters_1 = float(input("Enter the total liters required for Sunday: "))
desired_concentration_1 = float(input("Enter the desired concentration for Sunday: "))
solution_a_concentration_1 = 25
solution_b_concentration_1 = 50

x_1 = (desired_concentration_1 * total_liters_1 - solution_b_concentration_1 * total_liters_1) / (solution_a_concentration_1 - solution_b_concentration_1)
y_1 = total_liters_1 - x_1
order1 = x_1 - 3
order2 = y_1 - 3

print("\nFor Sunday:")
print(f"Liters of solution A needed: {x_1:.2f}")
if x_1 < 3:
    print("Solution (A) is available, can proceed.")
else:
    print(f"Solution (A) is not available, please order {order1:.2f} liter now.")
print(f"Liters of solution B needed: {y_1:.2f}")
if y_1 > 3:
    print(f"Solution (B) is not available, please order {order2:.2f} liter now.")
else:
    print("Solution (B) is available, can proceed.")

# Monday
total_liters_2 = float(input("\nEnter the total liters required for Monday: "))
desired_concentration_2 = float(input("Enter the desired concentration for Monday: "))
solution_a_concentration_2 = 15
solution_b_concentration_2 = 40

x_2 = (desired_concentration_2 * total_liters_2 - solution_b_concentration_2 * total_liters_2) / (solution_a_concentration_2 - solution_b_concentration_2)
y_2 = total_liters_2 - x_2
order3 = x_2 - 3
order4 = y_2 - 3

print("\nFor Monday:")
print(f"Liters of solution A needed: {x_2:.2f}")
if x_2 < 3:
    print("Solution (A) is available, can proceed.")
else:
    print(f"Solution (A) is not available, please order {order3:.2f} liter now.")
print(f"Liters of solution B needed: {y_2:.2f}")
if y_2 > 3:
    print(f"Solution (B) is not available, please order {order4:.2f} liter now.")
else:
    print("Solution (B) is available.")