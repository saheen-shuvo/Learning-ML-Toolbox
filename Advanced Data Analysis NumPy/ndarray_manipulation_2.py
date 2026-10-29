# Ndarray manipulation

# Transpose of an array: You can transpose an array using the T attribute. This will swap the rows and columns of the array.
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:")
print(arr1)

print("Transposed array:")
arr2 = arr1.T
print(arr2)

# array splitting: You can split an array into multiple sub-arrays using the split() method. The split() method takes the array to be split and the number of splits as arguments. The array will be split into equal parts along the specified axis.
arr3 = np.random.randint(1, 10, size=(10,))
print("Original array:")
print(arr3)

# array splitting
split_arr = np.array_split(arr3, 2)
print("Split array:")
print(split_arr)

# equal splitting: You can split an array into equal parts using the split() method. The number of splits must be a divisor of the size of the array along the specified axis.
split_arr = np.split(arr3, 2)
print("Split array:")
print(split_arr)