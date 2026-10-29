# Numpy Logical Functions

# The following functions are used to perform logical operations on ndarrays:
# np.logical_and(): Performs element-wise logical AND operation.
# np.logical_or(): Performs element-wise logical OR operation.
# np.logical_not(): Performs element-wise logical NOT operation.
# np.logical_xor(): Performs element-wise logical XOR operation.

import numpy as np

x =np.array([1, 2 , 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

# greater than: You can use the greater than operator (>) to compare two ndarrays element-wise. This will return a boolean ndarray indicating whether each element in the first array is greater than the corresponding element in the second array.
greater_than = x > y
print("Greater than:")
print(greater_than)

# using all(): You can use the np.all() function to check if all elements in a boolean ndarray are True. This function returns a single boolean value indicating whether all elements are True.
all_true = np.all(greater_than)

print("All elements are greater than:")
print(all_true)

# using any(): You can use the np.any() function to check if any element in a boolean ndarray is True. This function returns a single boolean value indicating whether any element is True.
any_true = np.any(greater_than)
print("Any element is greater than:")
print(any_true)

