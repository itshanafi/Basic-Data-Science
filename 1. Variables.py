# Product is the variable
# TV is the string literal
# "" is to differentiate the variables from values
product = "TV"
quantity = 2
price = 1455.99
available = True

if quantity > 0:
    print(f"The {product} is available for purchase. The price is ${price:.2f} for 1 {product}")
else:
    print(f"The {product} is currently out of stock.")

print("Product:", product)
print("Total:", quantity*price)


# type is a built function to know the type of class of the variables
print(type(product))

# type casting = convert data type to other type
quantity = "10"
price = "1455.99"
total = int(quantity) * float(price)
print(total)

# id is a function to show the adrress
number_x = 500
number_y = 500
print(id(number_x))
print(id(number_y))

string_x = "YOOO"
string_y = "YOOO"
print(id(string_x))
print(id(string_y))

# initialization
x = 0 # numeric initializer
x = "" # string initializer
x = None # no