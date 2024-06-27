'''
Write a program that calculates the sum of the first n terms of the harmonic series. Take the n as Input.
Hn = 1 + 1/2 + 1/3 + 1/4 .... + 1/n
'''

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += 1 / i

print(f"The sum of the first {n} terms of the harmonic series is {sum:.2f}")