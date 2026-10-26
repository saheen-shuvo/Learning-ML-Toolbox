# Data Type of Ndarray
# The data type of an ndarray is determined by the type of elements it contains. NumPy provides a wide range of data types, including integers, floats, complex numbers, and more. The data type can be specified when creating an array or inferred from the input data.
# The data type of an ndarray can be accessed using the dtype attribute. It returns a NumPy data type object that describes the type of elements in the array. The dtype attribute is useful for understanding the precision and memory requirements of the array's elements.

# using the dtype attribute, you can check the data type of an ndarray and perform operations accordingly. For example, if you have an array of integers, you can perform integer-specific operations, while for an array of floats, you can perform floating-point operations.

# upcasting: When performing operations on arrays with different data types, NumPy may upcast the data type to a more general type to avoid data loss. For example, if you add an integer array and a float array, the result will be a float array.
import numpy as np
arr1 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype)  # int32

arr2 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print(arr2.dtype)  # float64

arr3 = np.array([1, 2, 3], dtype=np.float64)
print(arr3.dtype)  # float64

print(arr3.dtype)  # float64

# astype: You can change the data type of an existing ndarray using the astype() method. This method creates a new array with the specified data type, leaving the original array unchanged.
arr4 = arr1.astype(np.float64)
print(arr4.dtype)  # float64