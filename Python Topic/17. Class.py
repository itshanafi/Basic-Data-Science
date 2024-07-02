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

"""
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
"""
'''
# Encapsulation
# defined in one place and not in multiple places
# Encapsulation is a process of binding data and code together in a single unit.
# data inside is not modified unexpectedly external code in a completely different part of the program
# attributes can be specified as public, proctected and private
# public: can be accessed from anywhere.
# Example: name
# protected: can be accessed from within the class and from child classes
# Example: _name
# private: can be accessed only from within the class
# Example: __name

class circle:
    def __init__(self, _radius):
        self._radius = 0
        if isinstance(_radius, int):
            self._radius = _radius
        else:
            raise ValueError("Radius must be an integer")

# Use getter and setter to contorl access to the object
    def getradius(self):
        return self._radius
    
    def setradius(self, _radius):
        if isinstance(_radius, int):
            self._radius = _radius
        else:
            raise ValueError("Radius must be an integer")

    radius = property(getradius, setradius)

    def area(self):
        self.areaC = 3.14 * self._radius ** 2
        return f"The area of the circle is {self.areaC}"
    
    def circumference(self):
        self.circumferenceC = 2 * 3.14 * self._radius
        return f"The circumference of the circle is {self.circumferenceC:.2f}"
    
mycircle = circle(20)
mycircle.radius = 30
print(mycircle)
print(mycircle.area())
print(mycircle.circumference())
'''


'''
# Inheritance
# Inheritance is a process where one class acquires the properties of another class.
# Inheritance provides reusability of a code. Reusability is a process in which you
# can create a new class that is already defined in another class.
# Inheritance is a way to create a new class using an existing class as a base.
# Inheritance is a way to reuse code.
# Inheritance is a way to create a hierarchy of classes.
# Inheritance is a way to create a relationship between classes.

# Has-a-relatioship

class Passport:
    def __init__(self, country, passportnum):
        self.country = country
        self.passportnum = passportnum

    def __str__(self):
        return f"\nCountry: {self.country} \nPassport Number: {self.passportnum}"

class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.icnumber = ''
        self.passport = None

    def __str__(self):
        message = f"Name: {self.name}\n"
        message = message + f"Address: {self.address} \n"
        message = message + f"Phone: {self.phone} \n"
        message = message + f"IC Number: {self.icnumber} \n"
        if self.passport != None:
            message = message + f"Passport: {self.passport}"
        return message

peter = Customer('Peter Parker', 'Johor, Malaysia','0123456789')
passport = Passport('Malaysia', 'A123A35')
peter.passport = passport
print(peter)
print(peter.__dict__)
'''

# Is-a-relationship

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.icnumber = ''
    

# alumni extend student class
class Alumni(Student):
    def __init__(self, name, age, gender, alumniyear):
        super().__init__(name, age, gender)
        self.icnumber = ''
        self.alumniyear = alumniyear

    def __str__(self):
        return f"Student name: {self.name} \nAge: {self.age} \nGender: {self.gender} \nIC Number: {self.icnumber} \
            \nAlumni Year: {self.alumniyear}"

alumni = Alumni("Peter Parker", 18, "Male", 2014)
print(alumni)




