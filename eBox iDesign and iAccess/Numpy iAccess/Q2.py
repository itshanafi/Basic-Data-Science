# Write a Python program to explore the characteristics of a dataset . Let us use the iris dataset defined in the sklearn library.
# Print the following details about the Iris Dataset --- Feature names, Target Names, First 5 rows of the iris data
# and the first 5 rows of the iris target vector.
# Refer the below link to get details about the iris dataset defined in sklearn library.
# https://scikit-learn.org/0.16/modules/generated/sklearn.datasets.load_iris.html
# Refer sample output for formatting specifications.
# Iris dataset from the sklearn library is considered as the input.
# Sample Output:
# Iris Feature Names
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# Iris Target Names
# ['setosa' 'versicolor' 'virginica']
# Iris Feature Matrix
# [[5.1 3.5 1.4 0.2]
#  [4.9 3.  1.4 0.2]
#  [4.7 3.2 1.3 0.2]
#  [4.6 3.1 1.5 0.2]
#  [5.  3.6 1.4 0.2]]
# Iris Target Vector
# [0 0 0 0 0]
# Type of Iris Feature Matrix
# class 'numpy.ndarray'
# Type of Iris Target Vector
# class 'numpy.ndarray'

import numpy as np
from sklearn.datasets import load_iris

def explore_iris_dataset():
    # Load the iris dataset
    iris = load_iris()
    
    # Print the feature names
    print("Iris Feature Names")
    print(iris.feature_names)
    
    # Print the target names
    print("Iris Target Names")
    print(iris.target_names)
    
    # Print the first 5 rows of the iris data
    print("Iris Feature Matrix")
    print(iris.data[:5])
    
    # Print the first 5 rows of the iris target vector
    print("Iris Target Vector")
    print(iris.target[:5])
    
    # Print the type of the iris feature matrix
    print("Type of Iris Feature Matrix")
    print(f"class 'numpy.{type(iris.data).__name__}'")
    
    # Print the type of the iris target vector
    print("Type of Iris Target Vector")
    print(f"class 'numpy.{type(iris.target).__name__}'")

def main():
    explore_iris_dataset()

if __name__ == "__main__":
    main()