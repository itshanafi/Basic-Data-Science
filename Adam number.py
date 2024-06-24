n = 153
rev = 0

if n >= 10:
    rev = (n % 10) * 10 + (n // 10) % 10
    if n >= 100:
        rev = (n % 10) * 100 + ((n // 10) % 10) * 10 + (n // 100) % 10
        if n >= 1000:
            rev = (n % 10) * 1000 + ((n // 10) % 10) * 100 + ((n // 100) % 10) * 10 + (n // 1000) % 10

n_sqr = n * n
rev_sqr = rev * rev

# Calculate reverse of the square of the number
if rev_sqr >= 10:
    rev_rev_sqr = (rev_sqr % 10) * 10 + (rev_sqr // 10) % 10
    if rev_sqr >= 100:
        rev_rev_sqr = (rev_sqr % 10) * 100 + ((rev_sqr // 10) % 10) * 10 + (rev_sqr // 100) % 10
        if rev_sqr >= 1000:
            rev_rev_sqr = (rev_sqr % 10) * 1000 + ((rev_sqr // 10) % 10) * 100 + ((rev_sqr // 100) % 10) * 10 + (rev_sqr // 1000) % 10
            if rev_sqr >= 10000:
                rev_rev_sqr = (rev_sqr % 10) * 10000 + ((rev_sqr // 10) % 10) * 1000 + ((rev_sqr // 100) % 10) * 100 + ((rev_sqr // 1000) % 10) * 10 + (rev_sqr // 10000) % 10

if n_sqr == rev_rev_sqr:
    print("Adam Number")
else:
    print("Not an Adam Number")

print("n_squared:", n_sqr)
print("rev_squared:", rev_rev_sqr)
