# Write a simple python function that returns twin primes less than 1000. If two consecutive odd numbers are both prime
# then they are known as twin primes.
# Pairs of primes that differ by 2. For example, 3 and 5, 5 and 7, 11 and 13, and 17 and 19 are twin primes.

def prime():
    primes = []
    for num in range(2, 1000):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def twin_primes():
    primes = prime()
    twin_primes = [(primes[i], primes[i+1]) for i in range(len(primes)-1) if primes[i+1] - primes[i] == 2]
    return twin_primes

print(twin_primes())
