import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV into a DataFrame
df = pd.read_csv('Medals.csv')

# Extract Total Medals
total_medals = df['Total']

# Configure plot settings
# plt.figure(figsize=(10, 6))

# Define the bins for the histogram
bins = [10, 20, 30, 40]

# Create the histogram
plt.hist(total_medals, bins=bins)

# set legend
plt.legend(['Total Medal Distribution'], loc='upper left')

# Set labels and title
plt.xlabel('Total Medals Range')
plt.ylabel('Count')
plt.title('Total Medals Histogram')

# Save the plot as plot6.png
plt.savefig('plot6.png')