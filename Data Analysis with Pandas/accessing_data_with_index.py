# Accessing data in dataframes using index in Pandas
import pandas as pd
# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [24, 27, 22, 32], 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Accessing a column using its name
print("\nAccessing 'Name' column:")
print(df['Name'])

# loc and iloc are used to access rows and columns in a DataFrame using labels and integer-based indexing respectively.
# Accessing a row using loc (label-based indexing)
print("\nAccessing row with index 1 using loc:")
print(df.loc[1])

# Accessing a row using iloc (integer-based indexing)
print("\nAccessing row with index 1 using iloc:")
print(df.iloc[1])

# single column access using loc
print("\nAccessing 'Age' column using loc:")
print(df.loc[:, 'Age'])

# single column access using iloc
print("\nAccessing 'Age' column using iloc:")
print(df.iloc[:, 1])

# multiple columns access using loc
print("\nAccessing 'Name' and 'City' columns using loc:")
print(df.loc[:, ['Name', 'City']])

# multiple columns access using iloc
print("\nAccessing 'Name' and 'City' columns using iloc:")
print(df.iloc[:, [0, 2]])

# row with column access using loc
print("\nAccessing row with index 2 and 'City' column using loc:")
print(df.loc[2, 'City'])

# row with column access using iloc
print("\nAccessing row with index 2 and 'City' column using iloc:")
print(df.iloc[2, 2])

print("\nDataFrame with 'Name' as index:")
print(df)

# changing the index of the DataFrame to 'Name'
df.set_index('Name', inplace=True)

# rename the index to 'Person'
df.index.name = 'Person'
print("\nDataFrame with 'Person' as index:")
print(df)