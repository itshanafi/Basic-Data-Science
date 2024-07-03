# # Syntax error is indention error
# # IndentationError: expected an indented block

# x = 10
# if x % 2 == 0:
# print("x is even")

# # Logical error 
# # The program runs but it does not do what you want it to do

# if x % 2 == 0:
#     print(f"given number is {x}")
# print("Even number")

# # Runtime error
# # The program runs but it crashes during execution

# principle = int(input("Principle: ").strip("RM"))
# period = int(input("Period: "))
# rate = int(input("Rate: ").strip("%"))
# interest = (principle * period * rate) / 100
# print(f"Interest: {interest}")

'''
while True:
    try:
        principle = int(input("Enter the principle amount: "))

        if principle <= 0:
            print("Principle amount must be a positive number.")
            continue

        period = int(input("Enter the period: "))
        if period <= 0:
            print("Period must be a positive number.")
            continue

        rate = int(input("Enter the rate (as a percentage): "))
        if rate <= 0:
            print("Rate must be a positive number.")
            continue

        if period == 0 or rate == 0:
            print("Period and rate cannot be zero.")
            continue

        interest = (principle * period * rate) / 100
        print(f"Interest: {interest}")
        break

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except Exception as e:
        print(f"Unexpected error: {e}")

    else:
        print("Thank you for using the program.")

    # this finally block will always executed
    finally:
        print("Thank you for using the program.")
'''


def keyboard(datatype, caption, errorMessage):
    value = None
    while True:
        try:
            value = datatype(input(caption))
            return value
        except ValueError:
            print(errorMessage)
        else:
            print("Thank you for using the program.")

def calculateInterest():
    principle = keyboard(int, "Enter the principle amount: ", "The amount of principle must be an integer")
    period = keyboard(int, "Enter the period: ", "Period must be an integer")
    rate = keyboard(float, "Enter the rate (as a percentage): ", "Rate must be a float")
    interest = (principle * period * rate) / 100

    print("Interest amount: ", interest)
    print("Total amount to be paid: ", interest + principle)

calculateInterest()