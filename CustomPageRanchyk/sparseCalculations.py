import numpy as np
import scipy.sparse as sp

MAGIC_COEF_FROM_GOOGLE = 0.15
PRECISION = 0.0001
MAX_ITER = 10000

def calculateMSCRMatrix(matrix):
    M = (1.0 - MAGIC_COEF_FROM_GOOGLE)*matrix
    dimension = matrix.shape[0]
    sMatrix = np.full((dimension, dimension), 1/dimension)
    M += MAGIC_COEF_FROM_GOOGLE*sMatrix
    return M


def powerRankSCRMethod(matrix):
    n = matrix.shape[1]
    A = np.copy(matrix)
    A.data /= np.take(A.sum(axis=0), A.indices)

    scores = np.ones(n, dtype=np.float32) * np.sqrt(A.sum() / (n * n))  # initial guess
    for i in range():
        scores = A @ scores
        nrm = np.linalg.norm(scores)
        scores /= nrm
        print(nrm)

    return scores
