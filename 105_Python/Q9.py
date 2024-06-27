'''
Write a program to convert a Roman numeral to an integer and also convert integer to Roman numeral
'''

# Print a menu to the user
print("Please choose:\n 1. Roman numeral to Integer.\n 2. Integer to Roman numeral")

# Get the user's choice
n = int(input())

# If the user chose to convert a Roman numeral to an integer
if n == 1:
    # Ask the user to enter a Roman numeral
    roman_numeral = input("Enter a Roman numeral: ")

    # Create a dictionary to map Roman numerals to their integer values
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Initialize the integer value to 0
    int_val = 0

    # Iterate over the Roman numeral
    for i in range(len(roman_numeral)):
        # If the current numeral is greater than the previous one, subtract the previous one's value
        if i > 0 and roman_numerals[roman_numeral[i]] > roman_numerals[roman_numeral[i - 1]]:
            int_val += roman_numerals[roman_numeral[i]] - 2 * roman_numerals[roman_numeral[i - 1]]
        # Otherwise, add the current numeral's value
        else:
            int_val += roman_numerals[roman_numeral[i]]

    # Print the integer value
    print("The integer value is ", int_val)

# If the user chose to convert an integer to a Roman numeral
elif n == 2:
    # Ask the user to enter an integer
    int_val = int(input("Enter an integer: "))

    # Create a list of Roman numeral values and their corresponding symbols
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    # Initialize the Roman numeral string
    roman_numeral = ''

    # Initialize the index to 0
    i = 0

    # While the integer value is greater than 0
    while int_val > 0:
        # Add the corresponding Roman numeral symbol to the string as many times as possible
        for _ in range(int_val // val[i]):
            roman_numeral += syb[i]
            int_val -= val[i]
        # Move to the next Roman numeral value
        i += 1

    # Print the Roman numeral
    print("The Roman numeral is ", roman_numeral)