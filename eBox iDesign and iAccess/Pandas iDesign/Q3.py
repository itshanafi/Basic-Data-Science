# Write a Python program to import specific columns from a given CSV file as a Pandas Data Frame.
# The 2 columns to be imported are sepal_length and sepal_width.
# The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.
# The input file is given as part of the template code.

import pandas as pd

def import_specific_columns():
    # Read the CSV file
    df = pd.read_csv('iris_with_header.csv')
    
    # Import the specified columns
    df_specific_columns = df[['sepal_length','sepal_width']]
    
    # Display the imported DataFrame
    print(df_specific_columns)

# Call the function to import the specific columns

import_specific_columns()

# Expected Output: