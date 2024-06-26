# Praveen who is working as Reservation Manager, asks for help from the development team to build a code that calculates the
# total cost to be charged on the customer by considering the date of Booking, date of vacating the hall, and cost per day.
# Imagine you are working in the development team and this task is assigned to you.  Write a program to calculate the total amount
# charged by the Hall Manager.
# Create a class Hall in ‘Hall.py’ with the following variables.
# Variable	DataType
# start_date	Date
# end_date	Date
# cost_per_day	int
# Use __init__() constructor to initialize the variables with respect to class.
# Use a 3 Argument constructor (start_date, end_date, cost_per_day).
# Use the following methods in Hall class to perform the corresponding operation.
# Method	Description
# no_days(self)	This method is used to calculate the number of days Item (say Hall) booked or used.
# cost(self,d)	Calculate the Total amount for Item (say Hall). Where ‘d’ is a number of days that is been calculated.
# (Call this method inside the no_days() method).
# Note:
# The format of the date is  "Jul 1 2014" (without quotes). 
# Input Format:
# The first line of the input is the Start date
# The Second line of the input is the end date. 
# The Third line of input consists of cost per day.
# Output Format:
# Display the number of days of stay and the total cost to be charged with the customer.
# Refer to sample input and output for formatting specifications.
# Note :
# → Output statements should be printed inside the Hall class and not in the Main class.
# → no_days() method should be called from the Main class and the cost() method should be called from no_days() method.
# All text in bold corresponds to input and the rest corresponds to output.
# Sample Input-Output:
# Enter Start time
# Dec 25 2017
# Enter the End time
# Dec 27 2017
# Enter the cost per day
# 1500
# Total number of days 2
# Total cost 3000 

# Main.py
import datetime
from Hall import Hall

def main():
    print("Enter Start time\n")
    start_date = input().strip()
    print("Enter the End time\n")
    end_date = input().strip()
    print("Enter the cost per day\n")
    cost_per_day = input("\n").strip()
    
    hall_booking = Hall(start_date, end_date, cost_per_day)
    total_cost = hall_booking.no_days()
    print(f"Total cost: {total_cost}")

if __name__ == "__main__":
    main()


# Hall.py
from datetime import datetime

class Hall:
    def __init__(self, start_date, end_date, cost_per_day):
        self.start_date = datetime.strptime(start_date, "%b %d %Y")
        self.end_date = datetime.strptime(end_date, "%b %d %Y")
        self.cost_per_day = int(cost_per_day)
    
    def no_days(self):
        delta = self.end_date - self.start_date
        num_days = delta.days + 1  # including both start and end dates
        total_cost = self.cost(num_days)  # calling cost method to calculate total cost
        print(f"Total number of days {num_days}")
        return total_cost
    
    def cost(self, days):
        total_cost = days * self.cost_per_day
        print(f"Total cost {total_cost}")
        return total_cost