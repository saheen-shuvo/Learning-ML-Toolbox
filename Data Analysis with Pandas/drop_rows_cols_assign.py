# Dropping rows and columns in a DataFrame using the drop() method
import pandas as pd
# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [24, 27, 22, 32], 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Dropping a row by index
df_dropped_row = df.drop(1)  # Drops the row with index 1
print("\nDataFrame after dropping row with index 1:")
print(df_dropped_row)

# Dropping multiple rows by index
df_dropped_rows = df.drop([0, 2])  # Drops the rows with index 0 and 2
print("\nDataFrame after dropping rows with index 0 and 2:")
print(df_dropped_rows)

# Dropping a column by name
df_dropped_col = df.drop('Age', axis=1)  # Drops the 'Age' column
print("\nDataFrame after dropping 'Age' column:")
print(df_dropped_col)

# Dropping multiple columns by name
df_dropped_cols = df.drop(['Age', 'City'], axis=1)  # Drops the 'Age' and 'City' columns
print("\nDataFrame after dropping 'Age' and 'City' columns:")
print(df_dropped_cols)

# iterrow() method to iterate over rows in a DataFrame
print("\nIterating over rows using iterrows():")    
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")
