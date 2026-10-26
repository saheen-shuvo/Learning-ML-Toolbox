# import numpy as np
import numpy as np

# 1d array
arr1 = np.array([1, 2, 3, 4, 5])
# type
print(type(arr1))  # <class 'numpy.ndarray'>
# shape
print(arr1.shape)  # (5,)
# dimention
print(arr1.ndim)  # 1

# 2nd array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# type
print(type(arr2))  # <class 'numpy.ndarray'>
# shape 
print(arr2.shape)  # (2, 3)
# dimention
print(arr2.ndim)  # 2

# 3d array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# type
print(type(arr3))  # <class 'numpy.ndarray'>
# shape
print(arr3.shape)  # (2, 2, 2)
# dimention
print(arr3.ndim)  # 3

# Array Attributes
# 1. shape: returns a tuple representing the dimensions of the array.
# 2. ndim: returns the number of axes (dimensions) of the array.
# 3. size: returns the total number of elements in the array.
# 4. dtype: returns the data type of the elements in the array.