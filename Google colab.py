import sys

if len(sys.argv) < 2:    # Check the correct number of  argument is provided
    print("Usage: python program_name.py <string>")
    sys.exit(1)

input_string = ' '.join(sys.argv[1:])   # Getting input string from command line arguments

words = input_string.split()    # Separate the string into individual string

print("Arguments :")
for word in words:  # Printing for each words
    print(word)

print("Number of arguments is", len(words)) # Printing the number of arguments contain in command line arguments

print(words)