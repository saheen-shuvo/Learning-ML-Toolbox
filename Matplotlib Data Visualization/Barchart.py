# Bar Chart: A graphical representation of categorical data using rectangular bars.

import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 9]

# Creating the bar chart
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
