# Ndarray Arithmetic Operators

import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

addition = x + y
print("Addition of x and y:")
print(addition)

subtraction = x - y
print("Subtraction of x and y:")
print(subtraction)

multiplication = x * y
print("Multiplication of x and y:")
print(multiplication)

division = x / y
print("Division of x and y:")
print(division)

# mathematical functions: NumPy provides a wide range of mathematical functions that can be applied to ndarrays. These functions include trigonometric functions, exponential functions, logarithmic functions, and more. You can apply these functions element-wise to the ndarray.

# trigonometric functions: You can apply trigonometric functions such as sine, cosine, and tangent to ndarrays using the np.sin(), np.cos(), and np.tan() functions, respectively. These functions take an ndarray as input and return a new ndarray with the computed values.
# radians: The trigonometric functions in NumPy expect the input values to be in radians. If your input values are in degrees, you can convert them to radians using the np.radians() function before applying the trigonometric functions.
sin_values = np.sin(x)
print("Sine values of x:")
print(sin_values)

cos_values = np.cos(x)
print("Cosine values of x:")
print(cos_values)

tan_values = np.tan(x)
print("Tangent values of x:")
print(tan_values)

# converting radian to degree: You can convert the computed trigonometric values from radians to degrees using the np.degrees() function. This function takes an ndarray of radian values as input and returns a new ndarray with the corresponding degree values.
deg_cos = np.rad2deg(cos_values)
print("Cosine values of x in degrees:")
print(deg_cos)

# find 10 base logarithm: You can compute the base-10 logarithm of an ndarray using the np.log10() function. This function takes an ndarray as input and returns a new ndarray with the computed logarithm values.
log10_values = np.log10(x)

# square root: You can compute the square root of an ndarray using the np.sqrt() function. This function takes an ndarray as input and returns a new ndarray with the computed square root values.
sqrt_values = np.sqrt(x)