import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [70000, 80000, 90000, 75000, 85000],
    'Joining_Date': ['2020-01-15', '2019-03-22', '2018-07-30', '2021-05-10', '2020-11-25']
}

df = pd.DataFrame(data)

# Convert Joining_Date to datetime
df['Joining_Date'] = pd.to_datetime(df['Joining_Date'])

# Calculate the number of days since joining
df['Days_Since_Joining'] = (pd.Timestamp.now() - df['Joining_Date']).dt.days

# Add joining year and month as separate columns
df['Joining_Year'] = df['Joining_Date'].dt.year
df['Joining_Month'] = df['Joining_Date'].dt.month