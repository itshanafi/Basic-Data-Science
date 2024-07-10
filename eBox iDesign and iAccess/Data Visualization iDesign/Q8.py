import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips', cache=True, data_home=r'\temp')

# Create count plot
plt.figure()
sns.countplot(x='day', hue='sex', data=tips, palette='magma')

# Set plot labels and title
plt.xlabel('day')
plt.ylabel('count')
plt.legend(loc='upper_left')

# Save the plot as a file
plt.savefig('splot6.png')