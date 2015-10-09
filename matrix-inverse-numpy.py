"""Creates a 10000x10000 random matrix and performs 10 matrix
inversions using numpy.
"""
import numpy as np

large_matrix = np.random.random((10000, 10000))
for i in range(10):
    np.linalg.inv(large_matrix)
