'''
A construction project requires two workers to complete. Worker A can complete the project in 12 hours,
while Worker B can complete the same project in 16 hours. How long will it take for both workers to complete
the project if they work together?
Another project requires Worker C, who can complete it in 8 hours, and Worker D, who can complete it in 10 hours.
How long will it take for both workers to complete this project if they work together?
Write a simple, generic Python program to assist in calculating the time required for two workers to complete
a project when working together. The program must take all these numbers (12, 16) as input and calculate the required time.
Finally, print the result. Please note that the same program must work for the second problem as well (8, 10).
'''

# For the first problem
workerA_hours = float(input("Enter the hours Worker A takes to complete the project: "))
workerB_hours = float(input("Enter the hours Worker B takes to complete the project: "))

total_hours = 1 / (1 / workerA_hours + 1 / workerB_hours)
print("When Worker A and Worker B work together, they will complete the project in", round(total_hours, 2), "hours.")

# For the second problem
workerC_hours = float(input("\nEnter the hours Worker C takes to complete the project: "))
workerD_hours = float(input("Enter the hours Worker D takes to complete the project: "))

total_hours = 1 / (1 / workerC_hours + 1 / workerD_hours)
print("When Worker C and Worker D work together, they will complete the project in", round(total_hours, 2), "hours.")
