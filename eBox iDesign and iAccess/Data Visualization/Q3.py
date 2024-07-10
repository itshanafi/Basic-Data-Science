import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV into a DataFrame
df = pd.read_csv('Medals.csv')

# Calculate total medals for each type
total_gold = df['Gold'].sum()
total_silver = df['Silver'].sum()
total_bronze = df['Bronze'].sum()

# Data for the pie chart
medal_counts = [total_gold, total_silver, total_bronze]
labels = ['Gold', 'Silver', 'Bronze']

# Configure plot settings
# plt.figure(figsize=(8, 8))
plt.pie(medal_counts, labels=labels, autopct='%1.1f%%')

# Set title and legend
plt.title('Medals data')
plt.legend(labels, loc='lower right')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Save the plot as plot7.png
plt.savefig('plot7.png')

# Display the plot
plt.show()
