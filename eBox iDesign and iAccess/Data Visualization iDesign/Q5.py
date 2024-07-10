import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips', cache=True, data_home=r'\temp')

# Create bar plot
plt.figure()
sns.barplot(x='day', y='total_bill', data=tips, palette='PuRd', ci=None)

# Set plot labels and title
plt.xlabel('day')
plt.ylabel('total_bill')

# Save the plot as a file
plt.savefig('splot3.png')

