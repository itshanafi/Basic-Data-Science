'''
Write a program that calculates the Body Mass Index (BMI) and categorizes it into different weight statuses.
The formula for BMI is weight / height^2, where weight is in kilograms and height is in meters.
Categories:
Underweight: BMI < 18.5
Normal weight: 18.5 <= BMI < 24.9
Overweight: 25 <= BMI < 29.9
Obesity: BMI >= 30
'''

weight = float(input("Please enter your weight (kg): "))
height = float(input("Please enter your height (m): "))

bmi = weight / (height ** 2)

if(bmi < 18.5):
  print(f"Your BMI is {bmi} and you are underweight.")

elif(bmi >= 18.5 and bmi < 24.9):
  print(f"Your BMI is {bmi} and you are normal weight.")

elif(bmi >= 25 and bmi < 29.9):
  print(f"Your BMI is {bmi} and you are overweight.")

else:
  print(f"Your BMI is {bmi} and you are obesity.")