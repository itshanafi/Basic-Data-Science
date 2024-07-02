# In every class there will be many properties

class Participant:

    course = "Python Data Science"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        count = 1
        print(self.first_name, self.last_name, count)

    def getFullName(self):
        return self.first_name + " " + self.last_name
    
hanafi = Participant("Hanafi", "Akmal")
print(hanafi.getFullName())
print(Participant.course)

# Class method
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
        
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
def main():
    harry = Employee("Harry", 455, "Instructor")
    rohan = Employee("Rohan", 455, "Student")
    print(harry.printdetails())
    print(rohan.printdetails())
    print(Employee.no_of_leaves)


if __name__ == "__main__":
    main()


# there is a class which has many method but no properties
# we can use class method to access the class properties

class Utility:
    @classmethod
    def printgood(cls):
        print("This is a good class method")

print(Utility.printgood())