import numpy as np


def matrix_transpose(A):
    arr = np.asarray(A)
    N, M = arr.shape
    result = np.empty((M, N), dtype=arr.dtype)
    for j in range(M):
        result[j, :] = arr[:, j]
    return result
