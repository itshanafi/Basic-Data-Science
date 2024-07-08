# Jack and Daniel are two army officers deployed in one under cover operation inside terrorist camp.
# They follow certain encryption strategy to communicate each other inside the camp .
# They follow string shuffling pattern as their encryption strategy. In this strategy,
# they can pass any message of any length, but only two words allowed. From that two words they need
# to find encrypted string which is a single word. Encryption principle followed here is to join first
# character of first word and last character of second word,then second character of first word and
# second last character of second string and so on to form a encrypted string. If there is no enough
# characters in any of string , add remaining characters in other string in encrypted string. 
# Help the officers to automate the process by writing a program.
# Note:
# No need to consider the decryption process.
# Input and Output Format:
# Input consists of two strings and output is a shuffled string which is a encrypted string. Refer sample input and output for formatting specifications.
# Sample input:
# hello
# hi
# Sample output:
# hiehllo

def encrypt(s1, s2):
    encrypted = []
    len1, len2 = len(s1), len(s2)
    
    min_len = min(len1, len2)
    
    # Interleave the characters as described
    for i in range(min_len):
        encrypted.append(s1[i])
        encrypted.append(s2[-(i+1)])
    
    # If any characters are left in the longer string, add them to the result
    if len1 > len2:
        encrypted.extend(s1[min_len:])
    elif len2 > len1:
        encrypted.extend(s2[:len2 - min_len][::-1])
    
    return ''.join(encrypted)

# Sample Input
s1 = input()
s2 = input()

# Encrypt and print the result
print(encrypt(s1, s2))


