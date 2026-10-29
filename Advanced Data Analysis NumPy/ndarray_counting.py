# Ndarray counting

# np.count_nonzero(): This function is used to count the number of non-zero elements in an array.

import numpy as np

# Example usage
arr = np.array([1, 0, 2, 0, 3])
print(np.count_nonzero(arr))  # Output: 3

value_greater_than_1 = np.count_nonzero(arr > 1)
print(value_greater_than_1)  # Output: 2

# np.unique(): This function is used to find the unique elements of an array and count their occurrences.
arr2 = np.array([1, 2, 2, 3, 3, 3])
unique_elements, counts = np.unique(arr2, return_counts=True)
print(unique_elements)  # Output: [1 2 3]
print(counts)  # Output: [1 2 3]