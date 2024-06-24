# List is a data structure or sequence
# List is mutable and ordered
# List is denoted using []
# List allow duplicate and can be modified
# Data in the list is heterogeneous and can be of different types

fruits = ["apple", "orange", "mango", "durian", "rambutan", "tomato", "papaya", "pear", "watermelon"]
quantity = [10, 20, 40, 30, 50, 70]

quality = quantity  # quality = quantity.copy()
quality[2] = 45 # it should be quality = []

#for i in quantity:              # deep copy
#    quality.append(quantity)

print(quantity)
print(quality)

fruits.append("mangosteen")
print(fruits)

if ("orange" in fruits):
    print(fruits.index("orange"))

# enumerate is a function used to find index of every item in the list
# the enumerate list is a list of tuple
# tuple have 2 values: 1. index 2. item
# tuple is denoted using ()
# tuple allows duplicate
# tuple is ordered and immutable
# Data in the tupple is heterogeneous and can be of different types

# fruits = ("apple", "orange", "mango", "durian", "rambutan", "tomato", "papaya", "pear", "watermelon")

fruitlist = tuple(enumerate(fruits))
print(fruitlist)

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# set is denoted {}
# set is unordered and mutable
# set does not allow duplicate
# Data in the set is heterogeneous and can be of different types
# set do not have index

fruits = {"apple", "orange", "mango", "durian", "rambutan", "tomato", "papaya", "pear", "watermelon"}
print(fruits)

for i in fruits:
    print(i)

fruits.add("melon")
print(fruits)

fruits.update(["banana", "guava"])
print(fruits)

fruits.pop() # randomly remove an item
print(fruits)

fruits.remove("watermelon")
print(fruits)

overseaFruits = {"apple", "orange", "banana", "mango"}
localFruits = {"durian", "rambutan", "cempedak", "mangosteen", "banana"}

print(overseaFruits.union(localFruits))
print(overseaFruits.intersection(localFruits))
print(overseaFruits.difference(localFruits))
print(localFruits.difference(overseaFruits))

content = '''
            Hi, hello good morning good evening good night
'''

word = content.split()
print(word)
print(set(word))


# dictonaries is denoted using {}
# dictionaries are mutable
# dictionaries are unordered
# dictionaries have key-value pairs
# keys must be unique and immutable
# values can be duplicate and mutable
# keys can be of any immutable type (string, int, float, tuple)
# values can be of any type (string, int, float, list, tuple, dictionary)
# dictonaties is also called as json
# json stands for java script object notation
# json is used to exchange data between web server and web application
# json is used to store data in no sql databases

detail = {
    "firstname" : "Peter",
    "lastname" : "Parker",
    "age" : 30,
    "city" : "New York",
    "hobbies" : ["reading", "gaming", "swimming"]
}
print(detail)
print(detail["firstname"])

detail["id number"] = "980987654322"
print(detail)