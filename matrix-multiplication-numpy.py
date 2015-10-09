"""Creates a 10000x10000 random matrix and performs 10 matrix-matrix
multiplications using numpy.
"""
import numpy as np

large_matrix = np.random.random((10000, 10000))
for i in range(10):
    large_matrix.dot(large_matrix)
