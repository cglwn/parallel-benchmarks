"""Creates a 10000x10000 random matrix and performs 10 matrix
inversions using Theano.
"""
import numpy as np
from theano import function
from theano.tensor.nlinalg import matrix_inverse

large_matrix = np.random.random((10000, 10000))
for i in range(10):
    matrix_inverse(large_matrix)
