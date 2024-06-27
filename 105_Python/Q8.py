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
        return ones[n - 1]
    elif n < 20:
        return teens[n - 10]
    elif n < 100:
        return tens[n // 10 - 2] + ('' if n % 10 == 0 else ' ' + ones[n % 10 - 1])
    elif n < 1000:
        return hundreds[n // 100 - 1] + ('' if n % 100 == 0 else ' and ' + num2word(n % 100))
    elif n < 10000:
        return thousands[n // 1000 - 1] + ('' if n % 1000 == 0 else ' ' + num2word(n % 1000))
    else:
        return "Number out of range"

n = int(input("Enter a number: "))
print(num2word(n))