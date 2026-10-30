# Pandas in Python is a powerful library for data manipulation and analysis. It provides two primary data structures: Series and DataFrame.

import pandas as pd

# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or SQL table.
# You can create a DataFrame from a dictionary, list of lists, or a NumPy array. 

# Importing data from a CSV file into a DataFrame
df = pd.read_csv('data.csv')

print("type of df:", type(df)) #pandas.core.frame.DataFrame
print("shape of df:", df.shape) #(rows, columns)
print("columns of df:", df.columns.tolist()) #['column1', 'column2', 'column3']
print("first 5 rows of df:") # First 5 rows of the DataFrame
print(df.head()) # First 5 rows of the DataFrame

# First column of the DataFrame
first_column = df.iloc[:, 0] # Selecting the first column using iloc
