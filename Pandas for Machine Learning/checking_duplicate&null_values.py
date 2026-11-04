import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "New York"],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales", "HR"],
    "Salary": [70000, 80000, 90000, 75000, 85000, 70000]
}

df = pd.DataFrame(data)

# Find unique values in the 'Name' column with null values
unique_names = df['Name'].unique()

# Check for unique values with null values in the 'City' column
unique_cities = df['City'].nunique()

# isnull() method to check for null values in the DataFrame
null_values = df.isnull().sum()

# hasnans() method to check for NaN values in the DataFrame
has_nan_values = df['Name'].hasnans

# Checking for duplicate values in the 'Name' column
duplicate_names = df[df.duplicated(subset='Name', keep=False)]

# Checking for duplicate values in the entire DataFrame
duplicate_rows = df[df.duplicated(keep=False)]

# removing duplicate rows from the DataFrame
df_no_duplicates = df.drop_duplicates()

# permanently removing duplicate rows from the DataFrame
df.drop_duplicates(inplace=True)

# removing duplicate rows based on the 'Name' column
df_no_duplicates_name = df.drop_duplicates(subset='Name')

# permanently removing duplicate rows based on the 'Name' column
df.drop_duplicates(subset='Name', inplace=True)

# removing duplicate rows based on the 'Name' and 'City' columns
df_no_duplicates_name_city = df.drop_duplicates(subset=['Name', 'City'])

# permanently removing duplicate rows based on the 'Name' and 'City' columns
df.drop_duplicates(subset=['Name', 'City'], inplace=True)

# removing duplicate rows based on the 'Name' and 'City' columns, keeping the last occurrence
df_no_duplicates_name_city_last = df.drop_duplicates(subset=['Name', 'City'], keep='last')

# permanently removing duplicate rows based on the 'Name' and 'City' columns, keeping the last occurrence
df.drop_duplicates(subset=['Name', 'City'], keep='last', inplace=True)

# Handling null values by dropping rows with null values
df_no_nulls = df.dropna()   

# dropna with how='all' to drop rows where all elements are null
df_no_nulls_all = df.dropna(how='all')

# Handling null values by filling null values with a specific value
df_filled_nulls = df.fillna(value={'Name': 'Unknown', 'City': 'Unknown', 'Department': 'Unknown', 'Salary': 0})