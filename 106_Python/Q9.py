# Write a simple Python function that takes a number(n) as a parameter. Then the function prints out the
# first n rows of Pascal's triangle. Note : Pascal's triangle is an arithmetic and
# geometric figure first imagined by Blaise Pascal

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