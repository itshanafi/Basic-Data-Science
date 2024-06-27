'''
Write a Python program that takes a single character as input and checks whether it is a vowel or consonant.
'''

char = str(input("Plase enter a single character: "))

if(char == 'a' or 'e' or 'i' or 'o' or 'u'):
  print(f"This character, {char} is a vowel.")

else:
  print(f"This character, {char} is a consonant.")