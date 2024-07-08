# Write a Python program to import the given CSV file as a Pandas Data Frame.
# The input file to be used is iris.csv file. Note that there is no header row in the input file.
# The input file is given as part of the template code.

import pandas as pd

# Define the column names
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_type']

# Load the CSV file into a DataFrame without a header row
df = pd.read_csv('iris.csv', header=None, names=column_names, skiprows=1)

# Display the DataFrame
print(df)
