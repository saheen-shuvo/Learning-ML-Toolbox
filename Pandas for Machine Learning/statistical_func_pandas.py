# Statistical functions in Pandas
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6]
})
# This script demonstrates various statistical functions available in the Pandas library for data analysis and manipulation. It covers basic statistical operations such as mean, median, mode, variance, standard deviation, and correlation. The examples provided will help you understand how to apply these functions to your datasets effectively.

# Mean: The mean is the average of a set of values. In Pandas, you can calculate the mean of a DataFrame or Series using the `mean()` method.
mean_salary = df['Salary'].mean()

# Median: The median is the middle value of a sorted list of numbers. In Pandas, you can calculate the median using the `median()` method.
median_salary = df['Salary'].median()

# Mode: The mode is the value that appears most frequently in a dataset. In Pandas, you can calculate the mode using the `mode()` method.
mode_salary = df['Salary'].mode()

# Maximum and Minimum: You can find the maximum and minimum values in a DataFrame or Series using the `max()` and `min()` methods, respectively.
max_salary = df['Salary'].max()
min_salary = df['Salary'].min()

# Variance: Variance measures how far a set of numbers are spread out from their average value. In Pandas, you can calculate the variance using the `var()` method.
variance_salary = df['Salary'].var()

# correlation: Correlation measures the relationship between two variables. In Pandas, you can calculate the correlation using the `corr()` method.
correlation = df.corr()

# Standard Deviation: Standard deviation is a measure of the amount of variation or dispersion in a set of values. In Pandas, you can calculate the standard deviation using the `std()` method.
std_dev_salary = df['Salary'].std()

# Skewness: Skewness measures the asymmetry of the probability distribution of a real-valued random variable. In Pandas, you can calculate skewness using the `skew()` method.
skewness_salary = df['Salary'].skew()