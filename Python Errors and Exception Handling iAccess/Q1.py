# An input list is given in the code template.
# Write a program to find the sum of first n values from the given list.
# For invalid ‘n’ values, raise an IndexError Exception and display the message shown in the sample output.
# Input and Output Format:
# Refer Sample Input and Output for formatting specifications.
# All text in bold corresponds to input and the rest corresponds to output.
# Sample Input and Output 1:
# [2, 3, 1, 5, 6, 7, 1]
# Enter n
# 5
# Sum = 17
# Sample Input and Output 2:
# [2, 3, 1, 5, 6, 7, 1]
# Enter n
# 10
# Index Value out of range

numlist = [2,3,1,5,6,7,1]
print(numlist)
n = int(input("Enter n\n"))
try:
    sum = 0
    for i in range(n):
        sum += numlist[i]
    print("Sum =",sum)

except IndexError:
    print("Index Value out of range")
