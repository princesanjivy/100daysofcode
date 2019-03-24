# @princesanjivy
# matrix addition using numpy 

import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

add = np.sum([matrix1, matrix2], axis=0)
print(add)