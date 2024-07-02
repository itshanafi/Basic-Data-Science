# Write a Python class that has two methods: getString and printString ,
# The getString accept a string from the user and printString prints the string in upper case.

class StringManipulator:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print(self.string.upper())


def main():
    obj = StringManipulator()
    obj.get_string()
    obj.print_string()


if __name__ == '__main__':
    main()
