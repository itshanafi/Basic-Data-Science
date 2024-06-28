# Write a program to illustrate Method Overloading in Python for the following College class.
# Create a class named College.
# There are no attributes in this class.
# Invoke the __str__() function two times with different different arguments to implement function overloading, as below:
# 1.  __str__(). print the College Id,College name ,city,state,pincode of a particular College.
# 2.  __str__(). print the College name, contactNumber and emailId of a particular College.
# Input and Output Format:
# Refer sample input and output for formatting specifications.
# All text in bold corresponds to input and the rest corresponds to output.

class College:
    def __init__(self, CollegeId, CollegeName, city=None, state=None, pincode=None, contactNumber=None, emailId=None):
        self.CollegeId = CollegeId
        self.CollegeName = CollegeName
        self.city = city
        self.state = state
        self.pincode = pincode
        self.contactNumber = contactNumber
        self.emailId = emailId
    
    def display_address(self):
        return f"id : {self.CollegeId},Name : {self.CollegeName},City : {self.city},State : {self.state},Pincode : {self.pincode}"
    
    def display_contact_details(self):
        return f"Name : {self.CollegeName},Contact Number : {self.contactNumber},Email : {self.emailId}"

# Main function to handle user input and interactions
def main():
    colleges = []  # List to store College objects
    
    while True:
        print("\n1. Enter College address and Display")
        print("2. Enter the contact details and Display")
        print("3. exit")
        
        choice = input("Enter your choice:\n")
        
        if choice == '1':
            CollegeId = input("Enter the College id\n")
            CollegeName = input("Enter the College name\n")
            city = input("Enter the City\n")
            state = input("Enter the State\n")
            pincode = input("Enter the Pincode\n")
            
            college = College(CollegeId, CollegeName, city, state, pincode)
            colleges.append(college)
            
            print(college.display_address())
        
        elif choice == '2':
            CollegeName = input("Enter the name of the College\n")
            contactNumber = input("Enter the contact number\n")
            emailId = input("Enter the email id\n")
            
            college = College(None, CollegeName, contactNumber=contactNumber, emailId=emailId)
            colleges.append(college)
            
            print(college.display_contact_details())
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
