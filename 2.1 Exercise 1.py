# Given is 76589. Reverse the number.
# Expected output is 98567

num = 76589
reversed_num = 0

remainder = num % 10
revs_number = reversed_num * 10 + remainder
num = num // 10

remainder = num % 10
revs_number = revs_number * 10 + remainder
num = num // 10

remainder = num % 10
revs_number = revs_number * 10 + remainder
num = num // 10

remainder = num % 10
revs_number = revs_number * 10 + remainder
num = num // 10

remainder = num % 10
revs_number = revs_number * 10 + remainder

print("The reverse number:", revs_number)


number = 76589
result = int(str(number)[::-1])

print(f"The reverse number: {result}")