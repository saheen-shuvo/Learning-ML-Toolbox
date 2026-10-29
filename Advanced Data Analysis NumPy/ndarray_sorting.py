# Ndarray Sorting

# inplace sorting: You can sort an array in-place using the sort() method. This will modify the original array and return None.
import numpy as np
arr1 = np.array([3, 1, 2, 5, 4])
print("Original array:")
print(arr1)

arr1.sort()
print("Array after in-place sorting:")
print(arr1)

# copy sorting: You can sort an array and return a new sorted array using the sorted() method. This will not modify the original array.
arr2 = np.array([3, 1, 2, 5, 4])
sorted_arr = np.sort(arr2)

# 2d array sorting: You can sort a 2D array along a specified axis using the sort() method. The axis parameter specifies the axis along which to sort the array. By default, the array is sorted along the last axis.
arr3 = np.array([[3, 1, 2], [5, 4, 6]])
print("Original 2D array:")
print(arr3)
arr3.sort(axis=0)
print("Array after sorting along axis 0:")
print(arr3)