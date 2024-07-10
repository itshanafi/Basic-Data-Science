import seaborn as sns
import matplotlib.pyplot as plt

# Load the car_crashes dataset
car_crashes = sns.load_dataset('car_crashes', cache=True, data_home=r'\temp')

# Set seaborn style
sns.set(style="whitegrid", rc={'grid.color': '.6', 'grid.linestyle': '-'})

# Create scatter plot
plt.figure()
plt.scatter(car_crashes['speeding'], car_crashes['alcohol'])

# # Set plot labels and title
# plt.xlabel('Speeding')
# plt.ylabel('Alcohol')
# plt.title('Scatter Plot of Speeding vs Alcohol')
# plt.legend(loc='upper left')

# Save the plot as a file
plt.savefig('splot1.png')

