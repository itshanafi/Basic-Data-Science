'''
Write a program that takes an integer input from the user and generates the Collatz sequence for that number.
The Collatz sequence is defined as follows:
start with a number n. If n is even, the next number is n/2. If n is odd, the next number is 3n + 1.
Repeat the process until n becomes 1.
'''

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Give me a number: ")
while n != 1:
    n = collatz(int(n))