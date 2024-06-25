fruits = ["apple", "orange", "mango", "durian", "rambutan", "tomato", "papaya", "pear", "watermelon"]

# the for loop can have 'else' part
# the code in the 'else' part will executed only when all the for loop are fully interated

# range of fruit[]
for i in range(len(fruits)):
    print(fruits[i])
    if(fruits == "durian"):
        break
else:
    print("All done")

# Multiplication table
for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i} x {j} = {i*j}")


# Take a number as input and print all the digit in the number using while-loop
num = int(input("Enter a number: "))
i = 0
while i < len(str(num)):
    print(int(str(num)[i]))
    i += 1

# the while loop also can have 'else' part
# only when the condition is failed
# the condition in while loop must resturn false
num = 2
count = 0
while count < 10:
    if num > 1:  
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:  
                break
        else:  
            print(num)
            count += 1
    num += 1

else:
    print("10 prime numbers are printed")


# continue keywood where it will continue the executing the following statement
multiplicant = [1, 2, 3, 4, 5, 6, 7, 8]
multiply = 7

for multiplicants in multiplicant:
    if multiplicants % 5 == 0:
        continue
    print(multiplicants, "x", multiply, "=", multiplicants*multiply)