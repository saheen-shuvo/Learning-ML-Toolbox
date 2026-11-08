# KDE Plot - Kernel Density Estimation Plot using Seaborn

import seaborn as sns # type: ignore
import matplotlib.pyplot as plt

# Sample data
data = {
    'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 14.78]
}

# Create a KDE plot
sns.kdeplot(data=data, x='total_bill', fill=True)

# Add labels and title
plt.xlabel('Total Bill')
plt.ylabel('Density')
plt.title('Kernel Density Estimation of Total Bills')

# Additional parameters like bandwidth can be adjusted as needed
plt.show()
