# Main.py
from Employee import Employee
from Developer import Developer
from Manager import Manager
from Utility import Utility


manager_list = []
manager_list.append(Manager("Arun",80000))
manager_list.append(Manager("Babu",100000))
manager_list.append(Manager("Chandru",60000))
manager_list.append(Manager("Deva",60000))

input_obj_list = []
choice = "yes"
while choice=="yes" :
    print("Menu\n1)Employee\n2)Developer\n")
    choice1 = input("Enter choice\n")
    if choice1 == "1" :
        input_str = input("Enter Employee details in comma separated format\n")
        name, pay = input_str.split(",")
        employee = Employee(name, pay)
        input_obj_list.append(employee)
        mgr_name = input("Enter manager name\n")
        for manager in manager_list :
            if manager.name == mgr_name :
                manager.add_employee(employee)
                
    else :
        input_str = input("Enter Developer details in comma separated format\n")
        name, pay, prog_lang = input_str.split(",")
        developer = Developer(name, pay, prog_lang)
        input_obj_list.append(developer)
        mgr_name = input("Enter manager name\n")
        for manager in manager_list :
            if manager.name == mgr_name :
                manager.add_employee(developer)
    choice = input("Do you want to continue? Type yes/no\n")

print("\nManager and Employee Allocation List")	
Utility.print_employees_under_each_manager(manager_list)
print("\n")


# Developer.py
from Employee import Employee

class Developer(Employee):
    
    def __init__(self, name, pay, prog_lang) :
        Employee.__init__(self, name, pay)
        self.prog_lang = prog_lang
        
    def __str__(self) :
        return "" + Employee.__str__(self) 


# Manager.py
from Employee import Employee
class Manager(Employee):

    def __init__(self, name, pay, employees=None):
        Employee.__init__(self, name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            

    def add_employee(self, emp):
        if isinstance(emp, Employee):
            self.employees.append(emp)
        else:
            raise ValueError("Only Employee instances can be added")

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            raise ValueError("Employee not found")


# Utility.py
from Employee import Employee
from Developer import Developer
from Manager import Manager

class Utility:
    @staticmethod
    def print_employees_under_each_manager(manager_list):
        for manager in manager_list:
            if not isinstance(manager, Manager):
                raise ValueError("Only Manager instances can be printed")
            print(f"\nManager Name: {manager.name}")
            if manager.employees:
                print("Employee List:")
                for employee in manager.employees:
                    print(employee.name)
            else:
                print("Employee List:")
                print("None")


# Employee.py
class Employee:

    def __init__(self, name, pay) :
        self._name = name
        self.pay = pay
        
    @property
    def name(self) :
        return self._name
    
    def __str__(self) :
        return self.name