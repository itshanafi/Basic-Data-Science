# Input Formate Specifications:

# The first line of input Contains Set1 integer.
# The second line of Input Contains set2  Integer.
# Output Format Specifications:

# The first line of Output contains set1 is a subset of set2 (True /False ).
# The second line of Output contains set2 is a subset of set1(True /False ).
# The next line of Output contains  set1 is a superset of set2(True /False ).
# The final line of Output contains set2 is a superset of set1(True /False ).
# Sample input and output will be shown below.

# Sample Input  1:
# 1,2,3,4,5,6
# 1,2,3

# Sample Output 1:
# False
# True
# True
# False

firstNum = set(input().split(','))
secondNum = set(input().split(','))

print(firstNum.issubset(secondNum))
print(secondNum.issubset(firstNum))
print(firstNum.issuperset(secondNum))
print(secondNum.issuperset(firstNum))


# Input and Output Format:
# Refer to sample input and output for formatting specifications.
# print “Client not found” if search not found. else print the details as in the mentioned format below.

# Note: All text in bold corresponds to the input and the rest corresponds to output.

# Sample Input and Output 1:
# Enter the number of clients
# 2
# Enter the details of the client 1
# Shri
# shri@mail.com
# 7346218
# Enter the details of the client 2
# Veena
# veena@mail.com
# 8639124
# Enter the passport number of the client to be searched
# 7346218
# Client Details
# Shri--shri@mail.com--7346218

# Sample Input and Output 2:
# Enter the number of clients
# 2
# Enter the details of the client 1
# Shri
# shri@mail.com
# 7346218
# Enter the details of the client 2
# Veena
# veena@mail.com
# 8639124
# Enter the passport number of the client to be searched
# 2346718
# Client not found

# Get the number of clients
n = int(input("Enter the number of clients\n"))

# Create a dictionary to store client details
clients = {}

# Get the details of each client
for i in range(1, n + 1):
    name = input(f"Enter the details of the client {i}\n")
    email = input()
    passport = input()
    clients[passport] = f"{name}--{email}--{passport}\n"

# Get the passport number of the client to be searched
passport_search = input("Enter the passport number of the client to be searched\n")

# Search for the client
if passport_search in clients:
    print("Client Details")
    print(clients[passport_search])
else:
    print("Client not found")