'''
Write a program to perform basic string compression using the counts of repeated characters (e.g., "aabcccccaaa" -> "a2b1c5a3").
'''

s = str(input("Enter any random string: "))
compressed = ""
count = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        compressed += s[i] + str(count)
        count = 1

if s:  # Check if the string is not empty
    compressed += s[-1] + str(count)

print("The compressed string is: ", compressed)