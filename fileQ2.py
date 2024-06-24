total_sum = 0

with open('user_input.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        total_sum += number

print(f"The sum of the integers you entered is: {total_sum}")

# iaccess
# Q1

with open("frequencyFile.txt", 'r') as file:
    sentence = file.read().lower()
    frequency = {}

    for char in sentence:
        if char.isalpha():  # only consider alphabetic characters
            frequency[char] = frequency.get(char, 0) + 1
            
    for char, freq in sorted(frequency.items()):
        print(f"{char}: {freq}")

# Q2

n = int(input())
data = []
for _ in range(n):
    name = input()
    salary = input()
    data.append(f"{name},{salary}")

with open("salaryData.csv", 'w') as file:
    file.write("\n".join(data))