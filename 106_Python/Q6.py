# A number is called perfect if the sum of proper divisors of that number is equal to the number.
# For example 28 is perfect number, since 1+2+4+7+14=28.
# Write a program to print all the perfect numbers in a given range

def checkPerfectNum(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n

def findPerfectNumbers(start, end):
    for num in range(start, end + 1):
        if checkPerfectNum(num):
            print(num)

start_range = 1
end_range = 10000
print(f"Perfect numbers in the range {start_range} to {end_range}:")
findPerfectNumbers(start_range, end_range)