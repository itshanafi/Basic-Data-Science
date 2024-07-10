import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips', cache=True, data_home=r'\temp')

# Create histogram with KDE
plt.figure()
sns.histplot(tips['total_bill'], kde=True)

# Set plot labels and title
plt.xlabel('total_bill')
plt.ylabel('Count')
# plt.title('Histogram of Total Bill with KDE')

# Save the plot as a file
plt.savefig('splot2.png')

