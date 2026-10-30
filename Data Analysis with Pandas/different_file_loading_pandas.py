# Different File loading in Pandas
import pandas as pd
# Loading data from a CSV file
df_csv = pd.read_csv('data.csv')
print("CSV DataFrame:")
print(df_csv)

# Excel file loading
df_excel = pd.read_excel('data.xlsx')
print("Excel DataFrame:")
print(df_excel)

# Parquet file loading
df_parquet = pd.read_parquet('data.parquet')
print("Parquet DataFrame:")
print(df_parquet)

# JSON file loading
df_json = pd.read_json('data.json')
print("JSON DataFrame:")
print(df_json)