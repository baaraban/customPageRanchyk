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
    def distance(v1, v2):
        v = np.squeeze(np.asarray(v1)) - np.squeeze(np.asarray(v2))
        v = v * v
        return np.sum(v);
    dimension = matrix.shape[0]
    previousAnswer = (dimension) * np.ones((dimension,1), dtype=np.float64)
    currentAnswer = (1 / dimension) * np.ones((dimension,1), dtype=np.float64)
    while distance(previousAnswer, currentAnswer) > PRECISION:
        previousAnswer = currentAnswer
        currentAnswer = matrix @ currentAnswer
    return currentAnswer
