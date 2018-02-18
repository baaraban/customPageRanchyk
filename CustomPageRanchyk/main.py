import loadingFromTextFile
import calculations
import resultsInterpretation
import sparseCalculations
import scipy.sparse as sp

matrix, dict = loadingFromTextFile.getMatrixAndDictionary("jaguar")

stochastic = calculations.calculateMMatrix(matrix)
result = calculations.powerRankMethod(stochastic)

cooMatrix = sp.coo_matrix(matrix)
coo = sparseCalculations.calculateMSCRMatrix(cooMatrix)
cooResult = sparseCalculations.powerRankSCRMethod(coo)

scrMatrix = sp.csr_matrix(matrix)
scr = sparseCalculations.calculateMSCRMatrix(scrMatrix)
scrResult = sparseCalculations.powerRankSCRMethod(scr)

interpretation = resultsInterpretation.getTopNArticles(10, result, dict)
interpretationSCR = resultsInterpretation.getTopNArticles(10, scrResult, dict)
interpretationCOO = resultsInterpretation.getTopNArticles(10, cooResult, dict)


for i in range(len(interpretation)):
    print(interpretation[i])

print("scr")

for i in range(len(interpretationSCR)):
    print(interpretationSCR[i])

print("coo")

for i in range(len(interpretationCOO)):
    print(interpretationCOO[i])






