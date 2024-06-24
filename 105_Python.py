'''
Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number,
and for the multiples of five, print "Buzz".
For numbers which are multiples of both three and five, print "FizzBuzz".
'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

'''
Write a program that takes an integer input from the user and generates the Collatz sequence for that number.
The Collatz sequence is defined as follows:
start with a number n. If n is even, the next number is n/2. If n is odd, the next number is 3n + 1.
Repeat the process until n becomes 1
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

'''
Write a program that takes two integers from the user and calculates their
greatest common divisor (GCD) using the Euclidean algorithm.
'''

def eulidean(A, B):
    while B != 0:
        A, B = B, A % B
    return A

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

print("The GCD of the two numbers is:", eulidean(first_num, second_num))

'''
Write a program that plays the game of Rock, Paper, Scissors with the user. The user makes a choice,
the program randomly chooses, and the winner is determined.
To generate random number use random module
import random
random.randint(1,3)
'''

# import random module
import random

print("ROCK VS PAPER VS SCISSOR GAME !")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice :"))

    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

        # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

        # print user choice
    print('Your choice is', choice_name.upper())
    print('Computer is thinking....')

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

     # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is ", comp_choice_name.upper())
    print(choice_name, 'Vs', comp_choice_name)
    
    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"
    # condition for winning
    if (choice == 1 and comp_choice == 2):
        print('paper wins =>', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'RocK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins =>', end="")
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>', end="")
        result = 'Scissors'
     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("LET'S PLAY AGAIN? (Y/N)")
    # if user input n or N then condition is True
    ans = input().lower()
    if ans == 'n':
        break

print("THANK YOU FOR PLAYING!")

'''
Write a program that randomly generates a number between 1 and 100. The user has to guess the number.
After each guess, the program tells the user whether the guess is too high, too low, or correct.
The game continues until the user guesses the correct number.
To generate random number use random module
import random
random.randint(1,3)
'''

import random

number_to_guess = random.randint(1, 100)
# number_to_guess = 50
guess = 0
while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")

print("YOU GUESS IT RIGHT !")

'''
Write a program that generates 10 perfect numbers.
Example
6: The divisors of 6 are 1, 2, 3, and 6.
The sum of its proper divisors (excluding 6 itself) is 1 + 2 + 3 = 6.
28: The divisors of 28 are 1, 2, 4, 7, 14, and 28.
The sum of its proper divisors (excluding 28 itself) is 1 + 2 + 4 + 7 + 14 = 28.
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

'''
Write a program that calculates the sum of the first n terms of the harmonic series. Take the n as Input.
Hn = 1 + 1/2 + 1/3 + 1/4 .... + 1/n
'''

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += 1 / i

print(f"The sum of the first {n} terms of the harmonic series is {sum:.2f}")

'''
Write a program that converts a number to its word representation (e.g., 123 to "one hundred twenty-three").
'''

ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
hundreds = ['one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']
thousands = ['one thousand', 'two thousand', 'three thousand', 'four thousand', 'five thousand', 'six thousand', 'seven thousand', 'eight thousand', 'nine thousand']

def num2word(n):
    if n < 10:
        return ones[n-1]
    elif n < 20:
        return teens[n-10]
    elif n < 100:
        return tens[n//10-2] + ('' if n%10==0 else ' ' + ones[n%10-1])
    elif n < 1000:
        return hundreds[n//100-1] + ('' if n%100==0 else ' and ' + num2word(n%100))
    elif n < 10000:
        return thousands[n//1000-1] + ('' if n%1000==0 else ' ' + num2word(n%1000))
    else:
        return "Number out of range"

n = int(input("Enter a number: "))
print(num2word(n))

'''
Write a program to convert a Roman numeral to an integer and also convert integer to Roman numeral
'''

print("Please choose:\n 1. Roman numeral to Integer.\n 2. Integer to Roman numeral")
n = int(input())
if n == 1:
    roman_numeral = input("Enter a Roman numeral: ")
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(roman_numeral)):
        if i > 0 and roman_numerals[roman_numeral[i]] > roman_numerals[roman_numeral[i - 1]]:
            int_val += roman_numerals[roman_numeral[i]] - 2 * roman_numerals[roman_numeral[i - 1]]
        else:
            int_val += roman_numerals[roman_numeral[i]]
    print("The integer value is ", int_val)
elif n == 2:
    int_val = int(input("Enter an integer: "))
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_numeral = ''
    i = 0
    while int_val > 0:
        for _ in range(int_val // val[i]):
            roman_numeral += syb[i]
            int_val -= val[i]
        i += 1
    print("The Roman numeral is ", roman_numeral)

'''
Write a program to perform basic string compression using the counts of repeated characters
(e.g., "aabcccccaaa" -> "a2b1c5a3")
'''

# Ask the user to input a random string
s = str(input("Enter any random string: "))

# Initialize an empty string to store the compressed result
compressed = ""

# Initialize a counter to count the consecutive occurrences of a character
count = 1

# Iterate through the input string, excluding the last character
for i in range(len(s) - 1):
    # If the current character is the same as the next one, increment the counter
    if s[i] == s[i + 1]:
        count += 1
    # If the current character is different from the next one, add the character and count to the compressed string, and reset the counter
    else:
        compressed += s[i] + str(count)
        count = 1

# If the input string is not empty, add the last character and its count to the compressed string
if s:  # Check if the string is not empty
    compressed += s[-1] + str(count)

# Print the compressed string
print("The compressed string is: ", compressed)
