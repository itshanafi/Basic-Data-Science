# Define a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0:
        return False  # Exclude even numbers greater than 2
    # Check odd factors up to square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Define a generator function to generate perfect numbers
def generate_perfect_numbers(n):
    count = 0  # Counter for the number of perfect numbers generated
    p = 2      # Start with the first Mersenne prime exponent
    while count < n:
        m = (1 << p) - 1  # Calculate Mersenne number 2^p - 1
        if is_prime(m):
            perfect_number = (1 << (p - 1)) * m  # Calculate the perfect number 2^(p-1) * m
            yield perfect_number
            count += 1
        p += 1  # Increment p to check the next Mersenne prime exponent

# Set n to 10 to generate the first 10 perfect numbers
n = 10
print(f"The first {n} perfect numbers are:")
# Iterate over the generator function to print the perfect numbers
for perfect_number in generate_perfect_numbers(n):
    print(perfect_number)
