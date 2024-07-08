# Write a Python program to read from a dataset . Let us use the iris dataset defined in the sklearn library.
# Seperate out the data part and print the top 3 rows from the data part in the iris dataset.
# Refer the below link to get details about the iris dataset defined in sklearn library.
# https://scikit-learn.org/0.16/modules/generated/sklearn.datasets.load_iris.html
# Refer sample output for formatting specifications.
# Iris dataset from the sklearn library is considered as the input.
# Sample Output:
# [[5.1 3.5 1.4 0.2]
#  [4.9 3.  1.4 0.2]
#  [4.7 3.2 1.3 0.2]]

from sklearn import datasets

def read_and_print_iris_data():
    iris = datasets.load_iris()
    data = iris.data
    print(data[:3])

def main():
    read_and_print_iris_data()

if __name__ == '__main__':
    main()
