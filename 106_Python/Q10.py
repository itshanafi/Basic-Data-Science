# Write a simple python function that accepts a hyphen-separated sequence of words
# as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def sort_words(words):
    return '-'.join(sorted(words.split('-')))

print(sort_words("green-red-yellow-black-white"))