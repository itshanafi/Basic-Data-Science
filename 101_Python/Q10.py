'''
Write a Python program that:
Converts the given binary 1011 to its decimal representation. Prints the decimal representation.
'''

bin = 1011

bin1 = bin % 10
print(bin1)
bin2 = (bin // 10) % 10
print(bin2)
bin3 = ((bin // 10) // 10) % 10
print(bin3)
bin4 = (((bin // 10) // 10) // 10) % 10
print(bin4)

dec = bin1 * (2 ** 0) + bin2 * (2 ** 1) + bin3 * (2 ** 2) + bin4 * (2 ** 3)

print(dec)