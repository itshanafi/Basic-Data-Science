# Write a Python program to rename a specific column in a Data Frame.
# Import the given CSV file as a Data Frame.
# Print the column names using columns attribute.
# Rename the column “species_type” to “SpeciesType”
# Print the column names using columns attribute.
# Print the entire contents of the Data Frame
# The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.
# The input file is given as part of the template code.

import pandas as pd

def main():
    # Read the CSV file
    df = pd.read_csv('iris_with_header.csv')
    
    # Print the column names
    print('Column Names\n', df.columns)
    
    # Rename the column
    df.rename(columns={'species_type': 'SpeciesType'}, inplace=True)
    
    # Print the updated column names
    print('Column Names after renaming\n', df.columns)
    
    # Print the entire Data Frame
    print("Data Frame")
    print(df)

if __name__ == '__main__':
    main()