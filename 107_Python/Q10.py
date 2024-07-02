# Write a Python class to check the validity of a string of parentheses,
# '(', ')', '{', '}', '[' and '].
# These brackets must be closed in the correct order, for example
# "()" and "()[]{}" are valid
# "[)", "({[)]" and "{{{" are invalid.

class checkValidity:
    def __init__(self, string):
        self.string = string

    def check(self):
        stack = []
        for i in self.string:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif i in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                else:
                    if i == ')' and stack[-1] == '(':
                        stack.pop()
                    elif i == '}' and stack[-1] == '{':
                        stack.pop()
                    elif i == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                if len(stack) == 0:
                    return True

def main():
    string = input("Enter a string: ")
    obj = checkValidity(string)
    if obj.check():
        print("Valid string")
    else:
        print("Invalid string")

if __name__ == '__main__':
    main()