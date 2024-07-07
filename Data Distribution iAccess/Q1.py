# Ramesh, the businessman had a list of data containing the overall transactions in a year.
# He wanted to calculate the statistics of his transactions i.e. calculating mean, median, and variance
# of his transactions to keep the track of his business growth over the years.
# Let's help Ramesh to calculate the mean, median and variance of the list of transactions given
# by writing code according to his requirements.
# Input format:
# Input consists of an array containing the overall transactions done in a year.
# Output Format:
# The output displays the mean, median and standard deviation of the transactions.
# Refer the sample Input and Output for formatting specifications
# Sample Input and Output:
# Enter the transactions done in each month for last year
# 4545
# 232
# 5565
# 1232
# 4512
# -7878
# -9698
# -7785
# 6624
# -5757
# 7597
# -774848
# Mean : -64638.25
# Median : 732.00
# Standard Deviation : 214218.97

def calculate_mean(transactions):
    return sum(transactions) / len(transactions)

def calculate_median(transactions):
    transactions.sort()
    n = len(transactions)
    if n % 2 == 0:
        median = (transactions[n//2 - 1] + transactions[n//2]) / 2
    else:
        median = transactions[n//2]
    return median

def calculate_variance(transactions, mean):
    return sum((x - mean) ** 2 for x in transactions) / len(transactions)

def calculate_standard_deviation(variance):
    return variance ** 0.5

def calculation():
    print("Enter the transactions done in each month for last year")
    transactions = []
    for _ in range(12):
        transaction = float(input())
        transactions.append(transaction)

    if len(transactions) == 0:
        print("No transactions provided.")
        return

    mean = calculate_mean(transactions)
    median = calculate_median(transactions)
    variance = calculate_variance(transactions, mean)
    std_dev = calculate_standard_deviation(variance)

    print(f"Mean : {round(mean, 2):.2f}")
    print(f"Median : {round(median, 2):.2f}")
    print(f"Standard Deviation : {round(std_dev, 2):.2f}")

calculation()
