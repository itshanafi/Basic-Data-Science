# input_string = input("Enter numbers separated by commas: ")

# numbers = []
# for num in input_string.split(','):
#     if int(num) not in numbers:
#         numbers.append(int(num))

# results = []

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         for k in range(j + 1, len(numbers)):
#             if numbers[i] + numbers[j] + numbers[k] == 100:
#                 combination = [numbers[i], numbers[j], numbers[k]]
#                 if combination not in results:
#                     results.append(combination)

# if results:
#     for result in results:
#         print(f"The three unique numbers = 100: {result[0]} + {result[1]} + {result[2]}")
# else:
#     print("There are no three unique numbers.")

input_string = input("Enter numbers separated by commas: ")

numbers = []
for num in input_string.split(','):
    if int(num) not in numbers:
        numbers.append(int(num))

combination_length = int(input("Enter the length of combinations: "))

results = []

def get_combinations(nums, length, current_combination=[]):
    if len(current_combination) == length:
        if sum(current_combination) == 100:
            results.append(list(current_combination))
    else:
        for i, num in enumerate(nums):
            get_combinations(nums[i+1:], length, current_combination + [num])

get_combinations(numbers, combination_length)

if results:
    for i, result in enumerate(results):
        print(f"Combination {i+1}: {result[0]} + {' + '.join(str(x) for x in result[1:])} = 100")
else:
    print("There are no combinations that add up to 100.")