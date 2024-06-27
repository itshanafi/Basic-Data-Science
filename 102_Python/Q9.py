'''
Write a Python program to check whether a given number is an Adam number.
An Adam number is a number for which the square of the number and the square of its reverse are
themselves reverses of each other. In other words, if you take a number, reverse it, square both the
original number and the reversed number, and the results are still reverse of each other, then the original number is called an Adam number.
'''

n = int(input("Please enter a number from 0 to 1000 to know wether it is Adam number or not: "))
rev = 0

if(n >= 10):
    rev = (n % 10) * 10 + (n // 10) % 10
    if(n >= 100):
        rev = (n % 10) * 100 + ((n // 10) % 10) * 10 + (n // 100) % 10
        if(n >= 1000):
            rev = (n % 10) * 1000 + ((n // 10) % 10) * 100 + ((n // 100) % 10) * 10 + (n // 1000) % 10

n_sqr = n * n
rev_sqr = rev * rev

# Calculate reverse of the reverse square of the number
if(rev_sqr >= 10):
    rev_rev_sqr = (rev_sqr % 10) * 10 + (rev_sqr // 10) % 10
    if(rev_sqr >= 100):
        rev_rev_sqr = (rev_sqr % 10) * 100 + ((rev_sqr // 10) % 10) * 10 + (rev_sqr // 100) % 10
        if(rev_sqr >= 1000):
            rev_rev_sqr = (rev_sqr % 10) * 1000 + ((rev_sqr // 10) % 10) * 100 + ((rev_sqr // 100) % 10) * 10 + (rev_sqr // 1000) % 10
            if(rev_sqr >= 10000):
                rev_rev_sqr = (rev_sqr % 10) * 10000 + ((rev_sqr // 10) % 10) * 1000 + ((rev_sqr // 100) % 10) * 100 + ((rev_sqr // 1000) % 10) * 10 + (rev_sqr // 10000) % 10

if(n_sqr == rev_rev_sqr):
    print(f"{n} is a Adam Number")
else:
    print(f"{n} is not a Adam Number")