'''
Write a python program to print first 10 terms in a Fibonacci series
'''

fibonacci_series = [0, 1]

for i in range(2, 10):
    next_term = fibonacci_series[i-1] + fibonacci_series[i-2]
    fibonacci_series.append(next_term)

print("The first 10 terms in the Fibonacci series are:")
for term in fibonacci_series:
    print(term)