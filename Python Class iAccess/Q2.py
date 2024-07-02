# [Note :
# Strictly adhere to the object oriented specifications given as a part of the problem statement.
# Use the same class names and member variable names. ]
# Create a base class named Student with the following  member variables / attributes  .
# Data Type	Variable Name
# Integer	id
# String	name
# String	department
# Integer	courseId
# Include a 4-argument constructor. The order of parameters passed to the constructor is id,name,department,courseId.
# Override a str() method to display the details of the class.
# Create a child class named StudentRating with the following  member variables / attributes  .
# Data Type	Variable Name
# Integer	id
# String	review
# Integer	stars
# Student	student
# Include a 4-argument constructor. The order of parameters passed to the constructor is
# id,review, stars, student(inherited from Student class.
# Override a str() method to display the details of the class.
# Input and Output Format:  
# Refer sample input and output for formatting specifications.  
# All text in bold corresponds to input and the rest corresponds to output.
# Sample Input and Output:
# Enter the student id
# 12
# Enter the student name
# Prakash
# Enter the department
# ECE
# Enter the course id
# 250
# Enter the Rating id
# 4
# Enter review
# Very good Student!!!
# Enter number of stars
# 5
# Student :
# Id :  12
# Name :  Prakash
# Department :  ECE
# Course Id :  250
# Rating ID :  4
# Review :  Very good Student!!!
# Rating Stars :  5

class Student:
    def __init__(self, id, name, department, course_id):
        self.id = id
        self.name = name
        self.department = department
        self.course_id = course_id

    def __str__(self):
        return f"Student :\nId : {self.id}\nName : {self.name}\nDepartment : {self.department}\nCourse Id : {self.course_id}"


class StudentRating(Student):
    def __init__(self, rating_id, review, stars, student):
        super().__init__(student.id, student.name, student.department, student.course_id)
        self.rating_id = rating_id
        self.review = review
        self.stars = stars

    def __str__(self):
        return f"{super().__str__()}\nRating ID : {self.rating_id}\nReview : {self.review}\nRating Stars : {self.stars}"


def main():
    id = int(input("Enter the student id\n"))
    name = input("Enter the student name\n")
    department = input("Enter the department\n")
    course_id = int(input("Enter the course id\n"))
    student = Student(id, name, department, course_id)
    rating_id = int(input("Enter the Rating id\n"))
    review = input("Enter review\n")
    stars = int(input("Enter number of stars\n"))
    student_rating = StudentRating(rating_id, review, stars, student)
    print(student_rating)


if __name__ == '__main__':
    main()