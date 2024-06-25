fruit = "apple"
fruit1, fruit2 = "apple", "orange"

fruits = ["apple", "orange", "mango", "durian", "rambutan", "tomato", "papaya", "pear", "watermelon"]
print(fruits[0]) # apple
print(fruits[-1]) # durian

# slicing method
# start_index:end_index. end index is not included
print(fruits[1:3]) # ['orange', 'mango']
print(fruits[:4])

# 3rd argument, step up argument
print(fruits[0:9:2])

# reverse order
print(fruits[::-1])

# count of fruits[]
print(len(fruits)) # 4

# separate of fruits[]
print(fruits[0], fruits[1], fruits[2], fruits[3]) # apple

# range of fruit[]
for i in range(len(fruits)):
    print(fruits[i])
    

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