'''
Initialize two variables, x = 0b10101100 and y = 0b11011001.
Write Python code to:
1. Extract the lower 4 bits from x.
2. Check if y is even or odd.
3. Clear the upper 4 bits of x.
4. Check if the 5th bit of y is set.
'''

x = 0b10101100
y = 0b11011001

lower_x = bin(x & 0b1111)
print(f"The lower 4 bits from x is {lower_x}")

upper_x = bin(x & 0b00001111)
print(f"The upper 4 bits of x is cleared, {upper_x}")

if(y & 1):
  print(f"{y} is odd")
else:
  print(f"{y} is even")

if(y & 0b10000):
  print(f"5th bit of {y} is set")
else:
  print(f"5th bit of {y} is not set")