# Write a Python class Employee with properties id, name, salary, and department and methods like _init_ calculateSalary,
# assignDepartment and _str_.
# Sample Employee Data:
# "E7876", "ADAMS", 50000, "ACCOUNTING"
# "E7499", "JONES", 45000, "RESEARCH"
# "E7900", "MARTIN", 50000, "SALES"
# "E7698", "SMITH", 55000, "OPERATIONS"
# Use 'assignDepartment' method to change the department of an employee.
# Use '_str_' method to print the details of an employee.
# Use 'calculateSalary' method takes two arguments: salary and hours_worked,
# which is the number of hours worked by the employee. If the number of hours worked is more than 50,
# the method computes overtime and adds it to the salary.
# Overtime is calculated as following formula: overtime = hours_worked - 50 Overtime amount = (overtime * (salary / 50))

class Employee:
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
    
    def assignDepartment(self, new_department):
        self.department = new_department
    
    def calculateSalary(self, hours_worked):
        if hours_worked > 50:
            overtime_hours = hours_worked - 50
            overtime_amount = overtime_hours * (self.salary / 50)
            total_salary = self.salary + overtime_amount
        else:
            total_salary = self.salary
        
        return total_salary
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}, Department: {self.department}"

def main():
    # Sample Employee Data
    employees = [
        Employee("E7876", "ADAMS", 50000, "ACCOUNTING"),
        Employee("E7499", "JONES", 45000, "RESEARCH"),
        Employee("E7900", "MARTIN", 50000, "SALES"),
        Employee("E7698", "SMITH", 55000, "OPERATIONS")
    ]
    
    # Print sample data
    print("Sample Employee Data:")
    for emp in employees:
        print(emp)
    print()
    
    # Prompt user for input
    name = input("Enter employee name to calculate salary: ")
    hours_worked = int(input(f"Enter hours worked by {name}: "))
    new_department = input(f"Enter new department for {name} (leave empty to keep current): ").strip()
    
    found = False
    for emp in employees:
        if emp.name.upper() == name.upper():
            if new_department:
                emp.assignDepartment(new_department)
            emp_salary = emp.calculateSalary(hours_worked)
            print(f"{emp.name}'s salary for {hours_worked} hours worked: ${emp_salary:.2f}")
            print(f"Current Department: {emp.department}")
            found = True
            break
    
    if not found:
        print(f"Employee with name '{name}' not found.")

if __name__ == "__main__":
    main()
