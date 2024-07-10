import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV into a DataFrame
df = pd.read_csv('Medals.csv')

# Extract Team names and Total Medals
teams = df['Team']
total_medals = df['Total']

# Configure plot settings
# plt.figure(figsize=(10, 6))  # Adjust figure size if necessary
plt.plot(teams, total_medals)

# Set labels and title
plt.xlabel('Team Name')
plt.ylabel('Total Number of Medals')
plt.title('Team-wise Total Medal Data')


# Save the plot as plot2.png
plt.savefig('plot1.png')

