# Write a Python program to perform the following tasks :
# Import the given csv file as Data Frame
# Display the entire contents of the Data Frame
# Display the Shape of the Data Frame
# Display the data types of the different columns in the Data Frame
# Display the number of columns under each data type in the Data Frame
# Display the Summary Statistics of the Data Frame
# The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.
# The input file is given as part of the template code.

import pandas as pd

# Read the csv file

df = pd.read_csv('iris_with_header.csv')

# Display the entire contents of the Data Frame
print("Data Frame")
print(df)

# Display the Shape of the Data Frame
print("Shape")
print(df.shape)

# Display the data types of the different columns in the Data Frame
print("Data Types")
print(df.dtypes)

# Display the number of columns under each data type in the Data Frame
print("Column Count under each dtype")
print(df.dtypes.value_counts())

# Display the Summary Statistics of the Data Frame
print("Summary Statistics")
print(df.describe())

# The input file to be used is iris_with_header.csv file. Note that there is a header row in the input file.
# The input file is given as part of the template code.
