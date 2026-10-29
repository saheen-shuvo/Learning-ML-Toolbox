# Ndarray searching

# np.where(): This function is used to find the indices of elements that satisfy a given condition.

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
# Find the indices of elements greater than 3
indices = np.where(arr1 > 3)
print("Indices of elements greater than 3:")
print(indices)

# Find the values of elements greater than 3
values = arr1[np.where(arr1 > 3)]
print("Values of elements greater than 3:")
print(values)

# np.nonzero(): This function is used to find the indices of non-zero elements in an array.
arr2 = np.array([0, 1, 2, 0, 3])
# Find the indices of non-zero elements
nonzero_indices = np.nonzero(arr2)
print("Indices of non-zero elements:")
print(nonzero_indices)

# Find the values of non-zero elements
nonzero_values = arr2[np.nonzero(arr2)]
print("Values of non-zero elements:")
print(nonzero_values)

# np.argmax(): This function is used to find the index of the maximum value in an array.
arr3 = np.array([1, 3, 2, 5, 4])
# Find the index of the maximum value
max_index = np.argmax(arr3)
print("Index of the maximum value:")
print(max_index)