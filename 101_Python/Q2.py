'''
Write a Python program that:
Prompts the user to enter a temperature in Celsius. Converts the temperature to Fahrenheit.
Prints the temperature in Fahrenheit. (Hint: The formula to convert Celsius to Fahrenheit is: F = C * 9/5 + 32)
'''

numCelsius = float(input("Please enter a temperature in Celsius to convert to Farenheit: "))

C = numCelsius
F = C * (9/5) + 32

print(f"The temperature of {C} to Farenheit is {F}.")