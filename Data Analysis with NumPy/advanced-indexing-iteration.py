# Advanced Indexing and Iteration in NumPy
import numpy as np  

# copy: When you create a new array by slicing or indexing, it creates a view of the original array, not a copy. This means that modifying the new array will also modify the original array. To create a copy of the array, you can use the copy() method.

arr1 = np.array([1, 2, 3, 4, 5])

# Create a view of the original array
arr2 = arr1[1:4]
print(arr2)  # Output: [2 3 4]

# create a copy of the original array
arr3 = arr1[1:4].copy()
print(arr3)  # Output: [2 3 4]

# Advanced Indexing: NumPy provides advanced indexing techniques that allow you to select elements from an array using boolean masks, integer arrays, or a combination of both. This allows for more complex and flexible indexing operations.

# Accessing muliple index
lst1 = [0, 2, 4]
arr4 = np.array([10, 20, 30, 40, 50])

# Accessing multiple indices using a list of indices
arr5 = arr4[lst1]
print(arr5)  # Output: [10 30 50]

# Boolean Indexing: You can use boolean masks to select elements from an array based on a condition. For example, you can create a boolean mask that selects all elements greater than a certain value.
arr4 = np.array([1, 2, 3, 4, 5])

# Create a boolean mask for elements greater than 3
mask = arr4 > 3
print(mask)  # Output: [False False False  True  True]

# Use the boolean mask to select elements from the array
arr5 = arr4[mask]
print(arr5)  # Output: [4 5]