# Ndarray indexing and slicing

# Create a 2x3 array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Indexing
print(arr[0, 0])  # Output: 1
print(arr[1, 2])  # Output: 6

# Slicing
print(arr[0, :])   # Output: [1 2 3]
print(arr[:, 1])   # Output: [2 5]
print(arr[0:2, 0:2])  # Output: [[1 2] [4 5]]

# 2d array slicing
portion = arr[0:2, 0:2]
print(portion)  # Output: [[1 2] [4 5]]