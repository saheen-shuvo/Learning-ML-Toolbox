# Histogram using Seaborn

import seaborn as sns # type: ignore
import matplotlib.pyplot as plt

# Sample data
data = {
    'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78]
}

# Create a histogram
sns.histplot(data=data, x='total_bill')

# Add labels and title
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.title('Distribution of Total Bills')

# bins, step, and other parameters can be adjusted as needed
plt.show()
