# Ndarray generation with random numbers

# Structure

import numpy as np

# np.random.rand(shape) - #Generates an array of the given shape with random numbers from a uniform distribution over [0, 1)

# Generate a 2x3 array of random numbers between 0 and 1
arr1 = np.random.random((2, 3))
print(arr1) #float numbers between 0 and 1

# Generate a 2x3 array of random integers between 1 and 10
arr2 = np.random.randint(1, 11, (2, 3))
print(arr2) 

# Generate a 2x3 array of random numbers from a normal distribution
arr3 = np.random.normal(0, 1, (2, 3))
print(arr3)