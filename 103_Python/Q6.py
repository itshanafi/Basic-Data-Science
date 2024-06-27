'''
Initialize two variables, x = 0b10101100 and y = 0b11010010.
Write Python code to:
1. Swap the values of x and y without using a temporary variable.
2. Toggle the 3rd and 5th bits of x.
3. Check if two given numbers a = 29 and b = 15 are different.
'''

x = 0b10101100
y = 0b11010010

x = x ^ y
print(bin(x))
y = x ^ y
print(bin(y))
x = x ^ y

print(f"After swapping, x = {bin(x)}")
print(f"After swapping, y = {bin(y)}")

x = y ^ (1 << 2)
x = x ^ (1 << 4)

print(f"After toggle 3rd and 5th bits of x, {bin(x)}")

a = 29
b = 15

# XOR operator (^) returns 1 if the corresponding bits of a and b are different, 0 otherwise
result = a ^ b

# If the result is non-zero, it means the numbers are different
if result:
    print("Numbers are different.")
else:
    print("Numbers are the same.")