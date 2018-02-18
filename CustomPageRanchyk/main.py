import loadingFromTextFile
import calculations
import resultsInterpretation
import sparseCalculations
import numpy
import scipy.sparse as sp

matrix, dict = loadingFromTextFile.getMatrixAndDictionary("jaguar")

# test = numpy.ones(shape=(3,3))
# test[0][0] = 0;
# test[0][1] = 0.5;
# test[0][2] = 0;
# test[1][0] = 0.5;
# test[1][1] = 0.5;
# test[1][2] = 0;
# test[2][0] = 0.5;
# test[2][1] = 0;
# test[2][2] = 0;
# print(test);

stochastic = calculations.calculateMMatrix(matrix)
result = calculations.powerRankMethod(stochastic)

# sparseMatrix = sp.csr_matrix(matrix)
# sparse = sparseCalculations.calculateMSCRMatrix(sparseMatrix)
# sparseResult = sparseCalculations.powerRankSCRMethod(sparse)

interpretation = resultsInterpretation.getTopNArticles(10, result, dict)

for i in range(len(interpretation)):
    print(interpretation[i])






