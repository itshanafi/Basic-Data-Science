# Your task is to Validate Credit Card Number
# Given a number determine whether or not it is valid per the Luhn formula.
# The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers,
# such as credit card numbers and Canadian Social Insurance Numbers.
# The task is to check if a given string is valid
# Valid credit card number
# 4539 3195 0343 6467
# The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling
# 4_3_ 3_9_ 0_4_ 6_6_
# If doubling the number results in a number greater than 9 then subtract 9 from the product. The results of our doubling:
# 8569 6195 0383 3437
# Then sum all of the digits:
# 8+5+6+9+6+1+9+5+0+3+8+3+3+4+3+7 = 80
# If the sum is evenly divisible by 10, then the number is valid. This number is valid!

'''
def checkLuhn(cardNo):
    cardNo = cardNo.replace(" ", "")  # remove spaces
    sum = 0
    for i in range(len(cardNo)-1,-1,-2):
        num = int(cardNo[i])
        if num*2 > 9:
            sum += (num*2) - 9
        else:
            sum += num*2
    
    for i in range(len(cardNo)-2,-1,-2):
        num = int(cardNo[i])
        sum += num
    
    if sum % 10 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    cardNo = input("Enter the card number: ")
    if checkLuhn(cardNo):
        print("Valid")
    else:
        print("Invalid")
'''

class LuhnAlgorithm:
    """Class to validate a number using Luhn algorithm."""
    
    def __init__(self, input_value: str) -> None:
        self.input_value = input_value.replace(' ', '')
    
    def last_digit_and_remaining_numbers(self) -> tuple:
        """Returns the last digit and the remaining numbers."""
        return int(self.input_value[-1]), self.input_value[:-1]
    
    def calculate_checksum(self, card_number: str) -> int:
        """Calculate the checksum using Luhn algorithm."""
        card_number = card_number.replace(" ", "")[::-1]
        checksum = 0
        for idx, num in enumerate(card_number):
            num = int(num)
            if idx % 2 != 0:  # Double every second digit
                doubled = num * 2
                if doubled > 9:  # If doubling results in a number greater than 9, adjust
                    doubled = doubled - 9
                checksum += doubled
            else:
                checksum += num  # Add non-doubled digits directly
        return checksum
    
    def verify(self) -> bool:
        """Verify a number using Luhn algorithm."""
        last_digit, remaining_numbers = self.last_digit_and_remaining_numbers()
        checksum = self.calculate_checksum(remaining_numbers)
        return (checksum + last_digit) % 10 == 0

def main():
    card_num = input("Enter your Credit Card No: ")
    lu = LuhnAlgorithm(card_num)
    if lu.verify():
        print("Valid")
    else:
        print("Invalid")

if __name__ == '__main__':
    main()
