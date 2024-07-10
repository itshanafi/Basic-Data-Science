import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips', cache=True, data_home=r'\temp')

# Create box plot
plt.figure()
sns.boxplot(x='day', y='total_bill', data=tips)

# Set plot labels and title
plt.xlabel('day')
plt.ylabel('total_bill')

# Save the plot as a file
plt.savefig('splot8.png')