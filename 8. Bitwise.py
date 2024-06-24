# to represent binaries in python by using 0b
# example: 711. separate the number and convert to binaries
# 7 = 111, 1 = 001, 1 = 001

filepermission = 0b111101001
print(filepermission)

print(bin(filepermission))

# permission for group only in 4, 5, 6 bits only
mask = 0b000111000

result = mask & filepermission
print(bin(result))

# shift to left 3x

print(bin(result >> 3))

#or
result2 = mask | filepermission
print(bin(result2))

# xor
content = 0b111001010
key = 0b101011000

encrypted = content ^ key
print(bin(encrypted))

decrypyted = encrypted ^ key
print(bin(decrypyted))

# Signed number (positive/negative)
# Max number in 8 bit = 2**7. 1 bit for signed (positive/negative)
# check the first bit of the binary number, if bit is 0 = positive and 1 = negative.
# 1s complement = flip the bits from 1 to 0 or 0 to 1
num = 5 # 101
print(bin(~num))
print(~num)

# 2s complement = get 1s complement + 1
print(bin(~num + 1))
print(~num + 1)

num = 0b11111010
# 1s complement
print(bin(~num + 1))
print(~num + 1)

# 2s complement
print(bin(~num))
print(~num)
