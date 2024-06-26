# Write a simple python function that takes a number as parameter and returns the prime factors of that number.
# Prime Factorization is finding which prime numbers multiply together to make the original number.
# Example: prime factors of 56 - 2, 2, 2, 7

def primeFactorization(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    return factors

num = int(input("Enter a number: "))
print(primeFactorization(num))