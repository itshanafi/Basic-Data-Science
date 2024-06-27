'''
Write a Python program that:
Prompts the user to enter their weight in kilograms and height in meters.
Calculates the Body Mass Index (BMI). Prints the BMI. (Hint: The formula to calculate BMI is: BMI = weight / (height * height))
'''

numFirst = float(input("Please enter your Height (m): "))
numSecond = float(input("Please enter your Weight (kg): "))

Height = numFirst
Weight = numSecond

BMI = Weight / (Height ** 2)

print(f"The BMI is {BMI}")