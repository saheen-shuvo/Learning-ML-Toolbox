import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales"],
    "Salary": [70000, 80000, 90000, 75000, 85000]
}

df = pd.DataFrame(data)

# Find cities containing the substring "New"
df.loc[df['City'].str.contains("New")] #case sensitive search

df.loc[df['City'].str.contains("new", case=False)] #case insensitive search

# using regular expressions to find cities starting with "Los"
df.loc[df['City'].str.contains(r"^Los")] 

# ends with "rk"
df.loc[df['City'].str.contains(r"rk$")]

# Name starts with vowels
df.loc[df['Name'].str.contains(r"^[AEIOU]")]

# City contains "New" or "Los"
df.loc[df['City'].str.contains(r"New|Los")]