'''
def calculateInterest(principle, period, rate):
    interest = (principle * period * rate) / 100
    return interest

def calculateTotalAmount(principle, interest):
    totalAmount = principle + interest
    return totalAmount

print((calculateInterest(1000, 1, 6)))
print(calculateTotalAmount(1000, calculateInterest(1000, 1, 6)))
'''

class student:
    def __init__(self, name, age, grade, student_ID):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_ID = student_ID

    def getGrade(self):
        return f"You got {self.grade} grade"
    
    def detailInfo(self):
        return f"Name: {self.name},\nAge: {self.age},\nGrade: {self.grade}, \nStudent ID: {self.student_ID}"
    
    def __str__(self):
        return f"Name: {self.name},\nAge: {self.age},\nGrade: {self.grade}, \nStudent ID: {self.student_ID}"
    

hanafi = student("Hanafi Akmal", "28 years old", 12, "MKE201090")
print(hanafi.getGrade())
print(hanafi.detailInfo())