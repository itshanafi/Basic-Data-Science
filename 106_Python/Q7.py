# Write a python function that takes 2 parameters lower and upper (range). Let the function returns pairs of amicable numbers in that range.
# Two different numbers are called amicable numbers if the sum of the proper divisors of each is equal to the other number.
# For example 220 and 284 are amicable numbers.
# For example if we call that function: amicableNumbers(1, 1000)
# The function must return: [220, 284]
# Why they are amicable numbers ?
# Sum of proper divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284
# Sum of proper divisors of 284 = 1+2+4+71+142 = 220


def sum_of_divisors(n):
    sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i * i != n:
                sum += i + n // i
            else:
                sum += i
    return sum
def amicable_numbers(lower, upper):
    amicable = []
    for i in range(lower, upper + 1):
        sum_i = sum_of_divisors(i)
        if sum_i != i and sum_i >= lower and sum_i <= upper and sum_of_divisors(sum_i) == i:
            amicable.append((i, sum_i))
    return amicable

print(amicable_numbers(1, 1000))