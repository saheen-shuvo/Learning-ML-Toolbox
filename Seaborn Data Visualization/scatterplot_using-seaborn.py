# Scatter Plot using Seaborn

import seaborn as sns # type: ignore
import matplotlib.pyplot as plt

# Sample data
data = {
    'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
    'tip': [1.01, 1.66, 3.50, 3.31, 3.61]
}

# Create a scatter plot
sns.scatterplot(data=data, x='total_bill', y='tip')

# Add labels and title
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Tips vs Total Bill')
