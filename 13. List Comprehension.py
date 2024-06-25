# List

fruits = ["apple", "orange", "mango", "durian", "rambutan", "tomato", "papaya", "pear", "watermelon"]

for fruit in fruits:
    print(fruit)

# we iterate through the list and create a new list
new_fruits = []
for fruit in fruits:
    new_fruits.append(fruit)
print("fruit: ", new_fruits)

prices = [10, 20, 40, 30, 50, 70]
pricesSST = []
for price in prices:
    pricesSST.append(price + (price * 0.06))
print("prices: ", pricesSST)


farenheit = [32, 43, 54, 65, 76, 87, 98]
celcius = []
for f in farenheit:
    celcius.append((f - 32) * 5/9)
print("celcius: ", celcius)

# number of items in the list newly created list is less than or same as original list
multiof3 = []
for num in range(0, 16):
    if num % 3 == 0:
        multiof3.append(num)
print("multiof3: ", multiof3)

number = [8, 4, 5, 1, 2, 21, 34, 76, 98, 12, 56]
even_num = []
for num in number:
    if num % 2 == 0:
        even_num.append(num)
print("even_num: ", even_num)

# iterate through a list of values and reduce it to a single values
number = [1, 2, 3, 4, 6]
sum_num = 0
for num in number:
    sum_num += num
print("sum_num: ", sum_num)

# iterate and create a new list
# by using list comprehension
fruits = ["apple", "orange", "mango", "durian", "rambutan"]
new_fruits = [fruit for fruit in fruits]
print("new_fruits: ", new_fruits)

price = [10, 20, 30, 40, 50, 60]
pricesSST = [price + (price * 0.06) for price in prices]
print("pricesSST: ", pricesSST)

farenheit = [32, 43, 54, 65, 76, 87, 98]
celcius = [(f - 32) * 5/9 for f in farenheit]
print(f"celcius: ", [f"{c:.2f}" for c in celcius])

number = [8, 4, 5, 1, 2, 21, 34, 76, 98, 12, 56]
even_num = [num for num in number if num % 2 == 0]
print("even_num: ", even_num)

number = [1, 2, 3, 4, 6]
sum_num = sum(num for num in number)  # or simply sum(number)
print("sum_num: ", sum_num)

# using a function called map(), reduce(), filter()
def calculateSST():
    prices = [10, 20, 30, 40, 50, 60]
    pricesSST = list(map(lambda price: price + (price * 0.06), prices))  # map(function, iterable)
    return pricesSST
print("pricesSST: ", calculateSST())

def ismultiof3():
    multiof3 = list(filter(lambda num: num % 3 == 0, range(1, 100)))  # filter(function, iterable)
    return multiof3
print("multiof3: ", ismultiof3())

def evenNum():
    numbers = [8, 4, 5, 1, 2, 21]
    even_num = list(filter(lambda num: num % 2 == 0, numbers))
    return even_num
print("even_num: ", evenNum())

# reduce() cannot use in list comprehension
from functools import reduce
def sumNum():
    numbers = [1, 2, 3, 4, 5, 6]
    sum_num = reduce(lambda x, y: x + y, numbers)  # reduce(function
    return sum_num
print("sum_num: ", sumNum())