import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales"],
    "Salary": [70000, 80000, 90000, 75000, 85000]
}

df = pd.DataFrame(data)

# Add a new Column with constant value
df['Country'] = 'USA'

# Add a new Column with values based on existing column
df['Salary in Thousands'] = df['Salary'] / 1000

# split the Name column into First Name and Last Name
df['First Name'] = df['Name'].str.split().str[0]
df['Last Name'] = df['Name'].str.split().str[1]

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_data.csv', index=False)

# Save the modified DataFrame to a new Excel file
df.to_excel('modified_data.xlsx', index=False)
