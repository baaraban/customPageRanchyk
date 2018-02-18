import os

from tqdm import tqdm

import loadingFromTextFile
import calculations
import resultsInterpretation
import sparseCalculations
import scipy.sparse as sp
import txtPreProcessing
import time


def countTime(func, args):
    start = time.time();
    result = func(args)
    end = time.time()
    return end - start, result


def getMilliSecondsString(seconds):
    return "{0:.2f}".format(seconds*1000) + " ms"

with open(txtPreProcessing.getFilePath("\\output\\", "results"), 'w') as outFile:
    for name in tqdm(os.listdir(txtPreProcessing.getFilePath(txtPreProcessing.DATA_PATH, ""))):
        adjacencyAndDictCalculations, result = countTime(loadingFromTextFile.getMatrixAndDictionary, name)
        matrix = result[0]
        dict = result[1]

        simpleMCalculationTime, stochastic = countTime(calculations.calculateMMatrix, matrix)

        simplePowerRankExecution, result = countTime(calculations.powerRankMethod, stochastic)

        cooBuildingTime, cooMatrix = countTime(sp.coo_matrix, matrix)
        cooMCalculationTime, coo = countTime(sparseCalculations.calculateMSCRMatrix, cooMatrix)
        cooPowerRankTime, cooResult = countTime(sparseCalculations.powerRankSCRMethod, coo)

        scrBuildingTime, scrMatrix = countTime(sp.csr_matrix, matrix)
        scrMCalculationTime, scr = countTime(sparseCalculations.calculateMSCRMatrix, scrMatrix)
        scrPowerRankTime, scrResult = countTime(sparseCalculations.powerRankSCRMethod, scr)

        stringOutput = ""
        stringOutput += '\n' + name + ' dataset'
        stringOutput += '\nAmount of entries: ' + str(len(dict)) + '\n'
        stringOutput += "BASIC INIT: " + getMilliSecondsString(adjacencyAndDictCalculations) + ";"
        stringOutput += "M MATRIX CALCULATION: " + getMilliSecondsString(simpleMCalculationTime) + ";"
        stringOutput += "POWER RANK EXECUTION: " + getMilliSecondsString(simplePowerRankExecution) + ";"
        stringOutput += '\n'
        stringOutput += "COO BUILDING TIME: " + getMilliSecondsString(cooBuildingTime) + ";"
        stringOutput += "COO M MATRIX CALCULATION TIME: " + getMilliSecondsString(cooMCalculationTime) + ";"
        stringOutput += "COO POWER RANK TIME: " + getMilliSecondsString(cooPowerRankTime) + ";"
        stringOutput += '\n'
        stringOutput += "SCR BUILDING TIME: " + getMilliSecondsString(scrBuildingTime) + ";"
        stringOutput += "SCR M MATRIX CALCULATION TIME: " + getMilliSecondsString(scrMCalculationTime) + ";"
        stringOutput += "SCR POWER RANK TIME: " + getMilliSecondsString(scrPowerRankTime) + ";"
        stringOutput += '\n'
        outFile.write(stringOutput)

        print(stringOutput)
        #
        # interpretation = resultsInterpretation.getTopNArticles(10, result, dict)
        # interpretationSCR = resultsInterpretation.getTopNArticles(10, scrResult, dict)
        # interpretationCOO = resultsInterpretation.getTopNArticles(10, cooResult, dict)






