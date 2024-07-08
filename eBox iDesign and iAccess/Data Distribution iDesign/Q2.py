# Write a python program to find the mean,std and var from pandas dataframe.
# Input Format
# Input is a file in CSV format.
# Output Format
# First line of output refers to mean of the column "pl"
# Second line of output refers to variance of the column "pl"
# Third line of output refers to standard deviation of the column "pl"
# Use 2 precisions for float
# Input File name-"iris.csv"
# Sample Input
# File Input(csv)
# Sample Output
# 5.79 
# 0.64 
# 0.80

import pandas as pd

def main():
    df = pd.read_csv('iris.csv')
    pl_mean = df['pl'].mean()
    pl_var = df['pl'].var()
    pl_std = df['pl'].std()
    print(f'{pl_mean:.2f}')
    print(f'{pl_var:.2f}')
    print(f'{pl_std:.2f}')

if __name__ == '__main__':
    main()