# Group by in pandas is a powerful tool for aggregating data based on certain criteria. It allows you to split your data into groups, apply a function to each group, and then combine the results back into a DataFrame.

import pandas as pd

data = {
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'Salary': [70000, 80000, 90000, 75000, 85000, 95000, 78000, 72000]
}

df = pd.DataFrame(data)

# Group by department
grouped = df.groupby('Department')

# Group by Department and calculate the average salary
grouped = df.groupby('Department')['Salary'].mean().reset_index()

# Group by Department and calculate the total salary
total_salary = df.groupby('Department')['Salary'].sum().reset_index()