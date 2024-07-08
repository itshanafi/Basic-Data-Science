# Write a python program to read from a csv file into a numpy array. Print the array.
# The name of the input csv file is sample_data.csv. It is provided as part of the template code.
# Refer sample input and output for formatting specifications.
# Sample Input:
# File Input. (sample_data.csv)
# Sample Output:
# [['Username' 'Identifier' 'First name' 'Last name']
#  ['booker12' '9012' 'Rachel' 'Booker']
#  ['grey07' '2070' 'Laura' 'Grey']
#  ['johnson81' '4081' 'Craig' 'Johnson']
#  ['jenkins46' '9346' 'Mary' 'Jenkins']
#  ['smith79' '5079' 'Jamie' 'Smith']]

import numpy as np

def read_csv_to_numpy_array(file_path):
    data = np.genfromtxt(file_path, delimiter=',', dtype=str)
    return data

if __name__ == "__main__":
    file_path = "sample_data.csv"
    array = read_csv_to_numpy_array(file_path)
    print(array)