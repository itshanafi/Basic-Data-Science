'''
Write a program that takes the lengths of three sides of a triangle and determines whether the
triangle is equilateral, isosceles, or scalene.
Equilateral: All three sides are equal.
Isosceles: Exactly two sides are equal.
Scalene: All three sides are different.
'''

len1 = int(input("Please enter the first lenght of sides of a triangle: "))
len2 = int(input("Please enter the second lenght of sides of a triangle: "))
len3 = int(input("Please enter the third lenght of sides of a triangle: "))

if(len1 == len2 and len1 == len3 and len2 == len3):
  print("This is a Equilateral triangle.")

elif(len1 == len2 or len1 == len3 or len2 == len3):
  print("This is a Isosceles triangle.")

else:
  print("This is a Scalene triangle.")