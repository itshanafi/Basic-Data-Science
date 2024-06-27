'''
Write a Python program that takes a score (between 0 and 100) as input and prints the corresponding grade based on the following criteria:
A for scores 90 and above
B for scores 80-89
C for scores 70-79
D for scores 60-69
F for scores below 60
'''

score = int(input("Please enter your score between 0 to 100 to know the grade: "))

if(score >= 90):
  print("Congrats! You got an A!")

elif(score >= 80 and score <= 89):
  print("Congrats! you got a B!")

elif(score >= 70 and score <= 79):
  print("Congrats! you got a C!")

elif(score >= 60 and score <= 69):
  print("Congrats! you got a D!")

else:
  print("WORK HARD! YOU GOT F!")