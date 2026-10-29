# Linear Algebra with NumPy
import numpy as np

study_hours = np.array([1, 2, 3, 4, 5])
mark_scores = np.array([10, 20, 30, 40, 50])

data = np.array([study_hours, mark_scores])

correlation = np.corrcoef(data)

print("Correlation Matrix:\n", correlation)

# multiplying using dot product
dot_product = np.dot(study_hours, mark_scores)
print("Dot Product:", dot_product)

# trace of a matrix
matrix = np.array([[1, 2], [3, 4]])
trace = np.trace(matrix)
print("Trace of the matrix:", trace)

# determinant of a matrix
determinant = np.linalg.det(matrix)
print("Determinant of the matrix:", determinant)

# rank of a matrix
rank = np.linalg.matrix_rank(matrix)