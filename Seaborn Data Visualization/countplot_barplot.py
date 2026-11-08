# Count Plot and Barplot in Seaborn


import matplotlib.pyplot as plt

# Sample data
data = {
    'category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
}

# Create a count plot
sns.countplot(data=data, x='category')

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Count of Each Category')

plt.show()

# Create a bar plot
sns.barplot(data=data, x='category', y='count')
# Add labels and title
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Bar Plot of Each Category')
plt.show() 