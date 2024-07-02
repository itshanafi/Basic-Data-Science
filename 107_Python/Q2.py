# An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter,
# however spaces and hyphens are allowed to appear multiple times.
# Examples of isograms:
# lumberjacks background downstream six-year-old
# The word isograms, however, is not an isogram, because the s repeats.
# Your task is to figure out if the user input is isogram

'''
def isogram(word):
    word = word.lower().replace(" ", "").replace("-", "").replace("_", "")
    if len(word) == len(set(word)):
        return "It is isogram"
    else:
        return "It is not isogram"

def main():
    word = input("Enter a word: ")
    result = (isogram(word))
    print(result)
    
if __name__ == '__main__':
    main()
'''

class IsogramChecker:
    def is_isogram(self, word):
        word = word.lower().replace(" ", "").replace("-", "").replace("_", "")
        if len(word) == len(set(word)):
            return "It is isogram"
        else:
            return "It is not isogram"

    def main(self):
        word = input("Enter a word: ")
        result = self.is_isogram(word)
        print(result)

if __name__ == '__main__':
    checker = IsogramChecker()
    checker.main()
