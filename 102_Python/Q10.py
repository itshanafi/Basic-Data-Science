'''
Write a Python program to check whether a given number is an Armstrong number.
An Armstrong number (also known as a Narcissistic number or a Pluperfect number) is a number
that is equal to the sum of its own digits each raised to the power of the number of digits.
For example, 153 is an Armstrong number because 1 ** 3 + 5 ** 3 + 3 ** 3 = 153
'''

n = int(input("Please enter a number limit from 0 to 9999: "))

if(n >= 1000 and n <= 9999):
    original_number = n
    # Get the last digit
    digit1 = original_number % 10
    digit1 = digit1 ** 4

    # Remove the last digit
    original_number = original_number // 10

    # Get the second-to-last digit
    digit2 = original_number % 10
    digit2 = digit2 ** 4

    # Remove the second-to-last digit
    original_number = original_number // 10

    # Get the third-to-last digit
    digit3 = original_number % 10
    digit3 = digit3 ** 4

    # Remove the third-to-last digit
    original_number = original_number // 10

    # Get the fourth-to-last digit
    digit4 = original_number % 10
    digit4 = digit4 ** 4

    # Calculate the sum
    armstrong_sum = digit1 + digit2 + digit3 + digit4

elif(n >= 100 and n <= 999):
    original_number = n

    # Get the last digit
    digit1 = original_number % 10
    digit1 = digit1 ** 3

    # Remove the last digit
    original_number = original_number // 10

    # Get the second-to-last digit
    digit2 = original_number % 10
    digit2 = digit2 ** 3

    # Remove the second-to-last digit
    original_number = original_number // 10

    # Get the third-to-last digit
    digit3 = original_number % 10
    digit3 = digit3 ** 3

    # Calculate the sum
    armstrong_sum = digit1 + digit2 + digit3

elif(n >= 10 and n <= 99):
    original_number = n

    # Get the last digit
    digit1 = original_number % 10
    digit1 = digit1 ** 2

    # Remove the last digit
    original_number = original_number // 10

    # Get the second-to-last digit
    digit2 = original_number % 10
    digit2 = digit2 ** 2

    # Calculate the sum
    armstrong_sum = digit1 + digit2

else:
    original_number = n

    # Get the last digit
    digit1 = original_number % 10
    digit1 = digit1 ** 1

    # Calculate the sum
    armstrong_sum = digit1

# Check if the number is an Armstrong number
if armstrong_sum == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")