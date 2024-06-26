# python function can access the variable
# defined in the outer scope or main context

x = 10
def sayX():
    print("1. ", x)

sayX()

def modify():
    x = 20
    print("2. ", x)
    # the value of the x only change inside the function
    # the value of the global of x didnt change

modify()
print("3. ", x)

# what if i dont want to create x as local variable
# and want to modify the global x
def modifyGlobal():
    global x
    
    print("4. ", x)
    x = 20

modifyGlobal()
print("5. ", x)

def authenticate():
    result = 10
    def checkResult():
        nonlocal result # Strictly use the result declared in the outer function
        result = 30
        print("6. ", result)
    
    checkResult()
    print("7. ", result)


authenticate()

