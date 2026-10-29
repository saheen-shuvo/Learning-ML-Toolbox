# Ndarray manipulation

# make a 5*10 array to 10*5 array
import numpy as np

arr1 = np.arange(50).reshape(5, 10)
print(arr1)

print("Transposed array:")
arr2 = arr1.T
print(arr2)

# Flattening an array: You can flatten a multi-dimensional array into a one-dimensional array using the flatten() method or the ravel() method. The flatten() method returns a copy of the original array, while the ravel() method returns a view of the original array.
arr3 = arr1.flatten()
print("Flattened array:")
print(arr3)

# Raveling an array: The ravel() method returns a view of the original array, which means that changes to the raveled array will affect the original array.
arr4 = arr1.ravel()
print("Raveled array:")
print(arr4)
print("Raveled array (view):")
print(arr4)

# Reshaping an array: You can reshape an array into a different shape using the reshape() method. The new shape must be compatible with the original shape, meaning that the total number of elements must remain the same.
arr5 = arr1.reshape(10, 5)
print("Reshaped array:")
print(arr5)

# row wise flattening: You can flatten an array row-wise using the flatten() method with the 'C' order parameter. This will flatten the array in a row-major order, meaning that the rows will be flattened first.
arr6 = arr1.flatten(order='C')
print("Row-wise flattened array:")
print(arr6)

# column wise flattening: You can flatten an array column-wise using the flatten() method with the 'F' order parameter. This will flatten the array in a column-major order, meaning that the columns will be flattened first.
arr7 = arr1.flatten(order='F')
print("Column-wise flattened array:")
print(arr7)

# Concatenating arrays: You can concatenate two or more arrays along a specified axis using the concatenate() method. The arrays must have the same shape along the concatenation axis.
arr6 = np.array([[1, 2], [3, 4]])
arr7 = np.array([[5, 6]])
arr8 = np.concatenate((arr6, arr7), axis=0)
print("Concatenated array:")
print(arr8)

# Row wise concatenation: You can concatenate two or more arrays row-wise using the vstack() method. This will stack the arrays vertically, meaning that the rows of the arrays will be stacked on top of each other.
arr9 = np.array([[1, 2], [3, 4]])
arr10 = np.array([[5, 6], [7, 8]])
arr11 = np.vstack((arr9, arr10))
print("Row-wise concatenated array:")
print(arr11) 

# Column wise concatenation: You can concatenate two or more arrays column-wise using the hstack() method. This will stack the arrays horizontally, meaning that the columns of the arrays will be stacked next to each other.
arr12 = np.array([[1, 2], [3, 4]])
arr13 = np.array([[5, 6], [7, 8]])
arr14 = np.hstack((arr12, arr13))
print("Column-wise concatenated array:")
print(arr14)

# row wise concatenation using axis: You can concatenate two or more arrays row-wise using the concatenate() method with axis=0. This will stack the arrays vertically, meaning that the rows of the arrays will be stacked on top of each other.
arr15 = np.array([[1, 2], [3, 4]])  
arr16 = np.array([[5, 6], [7, 8]])
arr17 = np.concatenate((arr15, arr16), axis=0)
print("Row-wise concatenated array (using axis=0):")
print(arr17)

# column wise concatenation using axis: You can concatenate two or more arrays column-wise using the concatenate() method with axis=1. This will stack the arrays horizontally, meaning that the columns of the arrays will be stacked next to each other.
arr18 = np.array([[1, 2], [3, 4]])
arr19 = np.array([[5, 6], [7, 8]])
arr20 = np.concatenate((arr18, arr19), axis=1)
print("Column-wise concatenated array (using axis=1):")
print(arr20)