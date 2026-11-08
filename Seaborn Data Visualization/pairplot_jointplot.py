# Pair plot and Joint Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset('iris')

# Pair plot
sns.pairplot(data, hue='species')
plt.show()

# Joint plot
sns.jointplot(data=data, x='sepal_length', y='sepal_width', hue='species')
plt.show() 