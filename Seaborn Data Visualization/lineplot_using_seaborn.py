# Seaborn data visualization - lineplot

import seaborn as sns # type: ignore
import matplotlib.pyplot as plt

# Sample data
data = {
    'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
    'tip': [1.01, 1.66, 3.50, 3.31, 3.61]
}

# Create a line plot
sns.lineplot(data=data, x='total_bill', y='tip', errorbar=None)

# Axes label vs Figure label: 
# Axes label is the label for the individual axes, while figure label is the label for the entire figure.
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Tips vs Total Bill')