def make_palindrome(s):
    return s[0:3] + s[-4::-1]

# Reading input
input_string = input().strip()  # Read and strip any leading/trailing whitespace

# Make input_string a palindrome if it's not already
result = make_palindrome(input_string)

# Print the result
print(result)