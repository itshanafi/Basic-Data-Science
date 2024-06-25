# find whether given number is positive, negative or zero
# find whether my business is making profit, loss or break even

expenses = 120000
sales = 15000

if sales > expenses:
    print("My business is making profit")
elif sales < expenses:
    print("My business is making loss")
else:
    print("My business is break even")

# expression using shothand if
x = 15
y = 10
op = "+"
result = x + y if (op == "+") else x - y