# Write a function that inputs a number and returns the product of digits of that number.
def product_of_digits(n):
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product

n = int(input("Enter a number: "))
print("Product of digits of", n, "is", product_of_digits(n))