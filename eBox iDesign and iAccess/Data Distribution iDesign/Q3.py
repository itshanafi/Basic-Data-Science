# Write a python program to find the mean,std and var from pandas dataframe.
# Input Format
# Input is a file in CSV format.
# Output Format
# First line of output refers to mean of the column "cyl"
# Second line of output refers to variance of the column "cyl"
# Third line of output refers to standard deviation of the column "cyl"
# Use 2 precisions for float
# Input File name-"cars.csv"
# Sample Input
# File Input(csv)
# Sample Output
# 6.50
# 2.40
# 1.55

import pandas as pd

def find_mean_std_var(file_path):
    df = pd.read_csv(file_path)
    mean = df["cyl"].mean()
    variance = df["cyl"].var()
    std = df["cyl"].std()
    print(f"{mean:.2f}")
    print(f"{variance:.2f}")
    print(f"{std:.2f}")
    return round(mean, 2), round(variance, 2), round(std, 2)

file_path = "cars.csv"

mean, variance, std = find_mean_std_var(file_path)

