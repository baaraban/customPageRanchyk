import numpy

MAGIC_COEF_FROM_GOOGLE = 0.15
PRECISION = 0.0001


def calculateMMatrix(matrix):
    M = (1.0 - MAGIC_COEF_FROM_GOOGLE)*matrix
    dimension = matrix.shape[0]
    SMatrix = numpy.full((dimension, dimension), 1/dimension)
    M += MAGIC_COEF_FROM_GOOGLE*SMatrix
    return M


def powerRankMethod(matrix):
    def distance(v1, v2):
        v = v1 - v2
        v = v * v
        return numpy.sum(v);

    dimension = matrix.shape[0]
    previousVector =((1/ dimension) + 1) * numpy.ones(dimension, dtype=numpy.float64)
    currentAnswer = (1/ dimension) * numpy.ones(dimension, dtype=numpy.float64)
    while distance(currentAnswer, previousVector) > PRECISION:
        previousVector = currentAnswer;
        currentAnswer = numpy.dot(matrix, currentAnswer);
    return currentAnswer;


