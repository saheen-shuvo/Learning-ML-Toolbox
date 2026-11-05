import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [70000, 80000, 90000, 75000, 85000]
}

df = pd.DataFrame(data)

# min max scaling
mn = df['Salary'].min()
mx = df['Salary'].max()

df['Salary_scaled'] = df['Salary'].apply(lambda x: (x - mn) / (mx - mn))

# Using custom built function
def scale_salary(x, min_val, max_val):
    return (x - min_val) / (max_val - min_val)

df['Salary_scaled_custom'] = df['Salary'].apply(lambda x: scale_salary(x, mn, mx))