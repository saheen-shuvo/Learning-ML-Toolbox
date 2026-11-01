# Sorting Data Frame in pandas

import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [24, 27, 22, 32], 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Sorting the DataFrame by Age in ascending order
df_sorted = df.sort_values(by='Age')
print(df_sorted)

# Sorting the DataFrame by Age in descending order
df_sorted_desc = df.sort_values(by='Age', ascending=False)
print(df_sorted_desc)

# Filtering Data Frame in pandas
# Filter the DataFrame to include only rows where Age is greater than 25
df_filtered = df[df['Age'] > 25]
print(df_filtered)

# Filter the DataFrame to include only rows where City is 'Chicago'
df_filtered_city = df[df['City'] == 'Chicago']
print(df_filtered_city)