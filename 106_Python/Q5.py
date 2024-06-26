# Write a function that takes a number as parameter. The function finds the proper divisors of that number and
# then finds the sum of proper divisors. Proper divisors of a number are those numbers by which the number is divisible,
# except the number itself.
# For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18

def divisor():
    num = int(input("Enter a number: "))
    divisors = [i for i in range(1, num) if num % i == 0]  # list comprehension to find proper divisors
    print("Proper divisors of", num, "are:", divisors)
    print("Sum of proper divisors of", num, "is:", sum(divisors))

divisor()