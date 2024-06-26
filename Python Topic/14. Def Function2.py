def authenticate(username, password):

    def simpleInterest(principal, period, rate):
        return (principal * period * rate) / 100
    if username == "admin" and password == "password":
        return simpleInterest

func = authenticate("admin", "password")
print("Interest ammount: ", func(1000, 1, 5))


# function without a name is also called annonymous function
# lambda function are writter in one line
# lambda arguments: expression
# lambda x, y: x + y
# lambda x, y: x * y
# lambda x, y: x / y

def sum(a, b):
    return a + b

sum = lambda a, b: a + b
print(sum(10, 20))