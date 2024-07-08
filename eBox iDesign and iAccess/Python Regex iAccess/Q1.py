# Use the re  module for Regular Expression
# Use the findAll method
# Extract all names from the given text. Use metacharacter
# Rules:
# 1) only alphabets
# 2) starts with upper-case
# 3) may contain surnames
# 4) may contain initials
# Input format:
# A single line input string consists of capitalized words in it.
# Output format:
# The output will be the words which are obeying the mentioned rules
# Sample Input 1:
# S.Vinoth Kumar and John Watson are friends with James
# Sample output 1:
# S.Vinoth Kumar 
# John Watson 
# James
# Sample Input 2:
# there were two friends named Sam and Jason
# Sample output 2:
# Sam
# Jason

import re

def main():
    text = input()
    names = re.findall(r'[A-Z](?:\.[A-Z])?[a-zA-Z]*(?: [A-Z](?:\.[A-Z])?[a-zA-Z]+)*', text)
    for name in names:
        print(name)

if __name__ == "__main__":
    main()