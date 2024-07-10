import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV into a DataFrame
df = pd.read_csv('Medals.csv')

rank = df['Rank']
total_rank = df['Rank_by_Total']

# Create scatter plot
plt.scatter(rank, total_rank, label='Rank Comparison')
plt.xlabel('Rank')
plt.ylabel('Rank_by_Total')
plt.title('Rank Comparison')
plt.legend(loc='upper left')
plt.savefig('plot4.png')

