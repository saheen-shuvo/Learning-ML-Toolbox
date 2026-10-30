# DataFrame from inbuilt data in Pandas
import pandas as pd

my_list = [['Alice', 24], ['Bob', 27], ['Charlie', 22]]

# Creating a DataFrame from a list of lists
df_from_list = pd.DataFrame(my_list)
print("DataFrame from a list of lists:")
print(df_from_list)

# Index and column names can be specified while creating the DataFrame
df_from_list_with_index = pd.DataFrame(my_list, index=['row1', 'row2', 'row3'], columns=['Name', 'Age'])
print("DataFrame with custom index and columns:")
print(df_from_list_with_index)

# passing a tuple to create a DataFrame
my_tuple = (['Alice', 24], ['Bob', 27], ['Charlie', 22])
df_from_tuple = pd.DataFrame(my_tuple, index=['row1', 'row2', 'row3'], columns=['Name', 'Age'])
print("DataFrame from a tuple:")
print(df_from_tuple)

# passing a dictionary to create a DataFrame
my_dict = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 27, 22]}
df_from_dict = pd.DataFrame(my_dict)
print("DataFrame from a dictionary:")
print(df_from_dict)