'''
Write a Python program that:
Prompts the user to enter the length and width of a rectangle. Calculates the area and perimeter of the rectangle.
Prints the area and perimeter.
'''

numLength = float(input("Please enter the Length: "))
numWidth = float(input("Please enter the Width: "))

L = numLength
W = numWidth

print("The perimeter of the rectangle is:", (2 * L) + (2 * W))
print("The area of the rectangle is:", L * W)