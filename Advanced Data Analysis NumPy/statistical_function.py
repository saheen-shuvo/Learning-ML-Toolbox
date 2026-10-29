# Data load from csv file
import numpy as np
data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)

math_marks = data[::, :1]  # Assuming math marks are in the first column

print("Math Marks:", math_marks.T)  # Transpose for better readability

max_math_marks = np.max(math_marks)
min_math_marks = np.min(math_marks)
average_math_marks = np.mean(math_marks)
median_math_marks = np.median(math_marks)
standard_deviation_math_marks = np.std(math_marks)