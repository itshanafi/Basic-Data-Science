# Write a program to print all prime numbers in the interval [a,b] (a and b, both inclusive).
# Input Format:
# Input consists of 2 integers which correspond to a and b. Assume that a is always less than or equal to b.
# Output Format:
# Refer sample output for details
# Sample Input 1:
# 2
# 15
# Sample Output 1:
# 2 3 5 7 11 13

num1 = int(input())
num2 = int(input())
for i in range(num1, num2+1):
    if i > 1:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")
