# Facet Plot using Seaborn: Figure-level function

import seaborn as sns # type: ignore
import matplotlib.pyplot as plt

# Sample data
data = {
    'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78],
    'tip': [1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00, 3.12, 1.96, 3.23],
    'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sat', 'Sat', 'Sat', 'Sat', 'Sat']
}

# Create a facet plot
sns.relplot(data=data, x='total_bill', y='tip', col='day', kind='scatter')

# Add labels and title
plt.subplots_adjust(top=0.85)
plt.suptitle('Tips vs Total Bill by Day')

