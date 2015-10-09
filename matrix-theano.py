import numpy as np
import theano.tensor as T
from theano import function

x = T.dmatrix('x')
y = T.dmatrix('y')
z = x.dot(y)
f = function([x, y], z)

large_matrix = np.random.random((10000, 10000))
print(f(large_matrix, large_matrix))
