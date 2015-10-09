"""Creates a 10000x10000 random matrix and performs 10 matrix-matrix
multiplications using Theano.
"""
import numpy as np
import theano.tensor as T
from theano import function

# Create the matrix multiplication function
x = T.dmatrix('x')
y = T.dmatrix('y')
z = x.dot(y)
matrix_multiply = function([x, y], z)

large_matrix = np.random.random((10000, 10000))
for i in range(10):
    matrix_multiply(large_matrix, large_matrix)
