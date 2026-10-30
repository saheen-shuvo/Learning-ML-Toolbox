# Pandas Basic Functionalities

import pandas as pd

# import csv file into a DataFrame
df = pd.read_csv('data.csv')

# first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head(5))

# last 5 rows of the DataFrame
print("Last 5 rows of the DataFrame:")
print(df.tail(5))

# column 
df.columns
print("Column names of the DataFrame:")
print(df.columns)

# columns in a list
columns_list = df.columns.tolist()
print("Columns in a list:")
print(columns_list)

# object type of the DataFrame
print("Object type of the DataFrame:")
print(type(df)) # pandas.core.frame.DataFrame

# index of the DataFrame
print("Index of the DataFrame:")
print(df.index)

# df info
print("DataFrame info:")
print(df.info()) 

# sample of the DataFrame
print("Sample of the DataFrame:")
print(df.sample(5)) # random sample of 5 rows from the DataFrame

# describe the DataFrame
print("Descriptive statistics of the DataFrame:")
print(df.describe())