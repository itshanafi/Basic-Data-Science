# declaring a function
# def is a keyword used to declare the function
# the function name is followed by paranthesis and colon ():
# the code is suppose to be inside the function

def sayHelloWorld():
    print("Hello World")
sayHelloWorld()

# some function require some input
# a variable or a place holder to keep the input called as parameter

def greet(argument1, argument2="Welcome to Python Programming"):
    if argument2 == "":
        argument2 = "Welcome to Python Programming"
    print(f"Hello {argument1}, {argument2}")

# Main program to interact with the user
print("Menu")
print("1. Name and Message")
print("2. Name")
choice = int(input())

if choice == 1:
    print("Enter the name")
    name = input().strip()      # name = input()    # .strip() is used to remove white space at the start and end of the string
    print("Enter the message")
    message = input().strip()   # message = input() # "  Hai  " > "Hai"
    greet(name, message)
elif choice == 2:
    print("Enter the name")
    name = input().strip()      # name = input()
    greet(name)
else:
    print("Invalid choice")


def buyLunch(foods, drinks):
    total_price = 0
    pack_food = []
    for food in foods:
        pack_food.append(food)
        if food == "Nasi":
            total_price += 2.00
        if food == "Ayam":
            total_price += 3.00
        if food == "Sayur":
            total_price += 1.50
    for food in drinks:
        pack_food.append(food)
        if food == "Ice Lemon Tea":
            total_price += 2.50
    return [total_price, pack_food]

result = buyLunch(["Nasi", "Ayam", "Sayur"], ["Ice Lemon Tea"])
print("The price is: ", result)

def calculateSI(principle, period = 2, rate = 3):
    interest = (principle * period * rate) / 100
    return interest

print(calculateSI(1000, 5, 2))
print(calculateSI(1000, 3))
print(calculateSI(1000))
print(calculateSI(1000, rate = 5))