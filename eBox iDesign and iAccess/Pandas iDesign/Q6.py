# Write a Python program to filter rows from a Data Frame based on a condition.
# Load iris data from the input file.
# Print the original Data Frame.
# Sort rows based on Sepal Length in ascending order and display the Data Frame.
# The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.
# The input file is given as part of the template code.

import pandas as pd

def filter_rows(input_file, condition):
    # Load the iris data from the input file
    df = pd.read_csv(input_file)
    
    # Print the original Data Frame
    print("Original DataFrame")
    print(df)
    
    # Sort rows based on Sepal Length in ascending order
    df_sorted = df.sort_values(by='sepal_length')
    
    # Filter rows based on the given condition
    df_filtered = df_sorted.query(condition)
    
    # Print the filtered Data Frame
    print("Sorted DataFrame")
    print(df_filtered)

def main():
    input_file = "iris_with_header.csv"
    condition = "sepal_length <= 5 | sepal_length > 5"
    filter_rows(input_file, condition)


if __name__ == '__main__':
    main()