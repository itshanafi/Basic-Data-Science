'''
Initialize two variables, a = 0b10101000 and b = 0b01010100.
Write Python code to:
1. Set the lower 4 bits of a.
2. Combine the bits of a and b using OR.
3. Create a mask to set the 2nd and 6th bits of a.
'''

a = 0b10101000
b = 0b01010100

lower_a = bin(a | 0b1111)
add = bin(a | b)
mask = 0b00100010

result = bin(a | mask)

print(lower_a)
print(add)
print(result)