# Write a simple Python function that takes a number(n) as a parameter. Then the function prints out the
# first n rows of Pascal's triangle. Note : Pascal's triangle is an arithmetic and
# geometric figure first imagined by Blaise Pascal

'''
# First method

def print_pascal(n):
    triangle = [[1 for _ in range(i+1)] for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    for row in triangle:
        print(' ' * (n - len(row)), end='')  # Add spaces for symmetry
        print(' '.join(str(num) for num in row))
    print()

n = int(input("Enter a number to do Pascal's Triangle: "))
print_pascal(n)

'''

# Second Method

def print_pascal(n):
    # Initialize Pascal's triangle with appropriate spaces
    pascal_triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
        pascal_triangle.append(row)
    
    # Find the maximum width of the last row (for formatting)
    max_width = len(' '.join(map(str, pascal_triangle[-1])))
    
    # Print Pascal's triangle with center alignment
    for row in pascal_triangle:
        # Calculate leading spaces for centering
        num_spaces = (max_width - len(' '.join(map(str, row)))) // 2
        print(' ' * num_spaces, end='')
        
        # Print each element of the row
        for num in row:
            print(num, end=' ')
        
        print()  # Move to the next line

n = int(input("Enter the number of rows: "))
print_pascal(n)
