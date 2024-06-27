'''
Print first 10 prime numbers using for loop
'''

num = 2
count = 0
while count < 10:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
            count += 1
    num += 1