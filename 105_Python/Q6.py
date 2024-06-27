'''
Write a program that generates 10 perfect numbers.
Example
6: The divisors of 6 are 1, 2, 3, and 6. The sum of its proper divisors (excluding 6 itself) is 1 + 2 + 3 = 6.
28: The divisors of 28 are 1, 2, 4, 7, 14, and 28. The sum of its proper divisors (excluding 28 itself) is 1 + 2 + 4 + 7 + 14 = 28.
'''

import random
import timeit

start = timeit.default_timer()

def miller_rabin(n, k=5):
    """
    Miller-Rabin primality test to determine if n is likely prime.
    Parameters:
    - n: The number to be tested for primality.
    - k: The number of rounds of testing (default is 5).
    Returns:
    - True if n is likely prime, False otherwise.
    """

    # Base cases for small values of n
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d where d is odd
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Miller-Rabin test function
    def miller_test(a, d, n):
        """
        Inner function to perform Miller-Rabin test for a given base a.
        Parameters:
        - a: Base to test if it is a witness for n's compositeness.
        - d: Odd integer such that n-1 = 2^r * d.
        - n: Number to test for primality.
        Returns:
        - True if a is a witness for n's compositeness, False otherwise.
        """
        # Compute a^d % n
        x = pow(a, d, n)

        # If the result is 1 or n-1, a may be a witness for n's primality
        if x == 1 or x == n - 1:
            return True

        # Repeat squaring x until d becomes n-1 or find a non-trivial square root of 1
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == n - 1:
                return True
            if x == 1:
                return False

        # If 'a' is a strong witness for n's compositeness return False
        return False

    # Perform k rounds of Miller-Rabin test with random bases a
    for _ in range(k):
        a = random.randint(2, n - 2)
        if not miller_test(a, d, n):
            return False

    # If all rounds pass, n is likely prime
    return True


# Updated is_prime function using Miller-Rabin test with caching
def is_prime(n, prime_cache):
    if n in prime_cache:
        return prime_cache[n]
    if n <= 3:
        prime_cache[n] = n > 1
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        prime_cache[n] = False
        return False
    prime_cache[n] = miller_rabin(n)  # Use Miller-Rabin test for larger numbers
    return prime_cache[n]


# Generator function to generate perfect numbers
def generate_perfect_numbers(n):
    count = 0
    p = 2
    prime_cache = {}  # Cache for storing prime numbers
    while count < n:
        m = (1 << p) - 1  # Calculate Mersenne number 2^p - 1
        if is_prime(m, prime_cache):
            perfect_number = (1 << (p - 1)) * m  # Calculate the perfect number 2^(p-1) * m
            yield perfect_number
            count += 1
        p += 1

# Set n to 10 to generate the first 10 perfect numbers
n = 10
print(f"The first {n} perfect numbers are:")
for idx, perfect_number in enumerate(generate_perfect_numbers(n), start=1):
    print(f"Perfect number {idx}: {perfect_number}")

end = timeit.default_timer()
print(f"runtime:{end - start:.2f}s")