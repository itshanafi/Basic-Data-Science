# A pangram is a sentence using every letter of the alphabet at least once.
# It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
# For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
# Example: The quick brown fox jumps over the lazy dog.
# Your task is to figure out if a sentence is a pangram.

'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
sentence = set(sentence.replace(" ", ""))  # remove spaces and convert to set

if set(alphabet).issubset(sentence):
    print("Pangram")
else:
    print("Not a pangram")
'''

class PangramChecker:
    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def is_pangram(self, sentence):
        sentence = sentence.lower()
        sentence = set(sentence.replace(" ", ""))  # remove spaces and convert to set

        if set(self.alphabet).issubset(sentence):
            return True
        else:
            return False

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    checker = PangramChecker()
    
    if checker.is_pangram(sentence):
        print("Pangram")
    else:
        print("Not a pangram")
