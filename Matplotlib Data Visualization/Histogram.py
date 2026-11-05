# Histogram: A graphical representation of the distribution of a dataset.

# Left-skewed distribution: The tail on the left side of the distribution is longer or fatter than the right side.

# Right-skewed distribution: The tail on the right side of the distribution is longer or fatter than the left side.

# Normal distribution: The distribution is symmetric and follows a bell-shaped curve.

# creating a histogram using matplotlib
import matplotlib.pyplot as plt

# Sample data
data = [12, 15, 12, 10, 8, 9, 15, 18, 20, 22, 25, 30, 35, 40]

# Creating the histogram
plt.hist(data, bins=5, color='blue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')