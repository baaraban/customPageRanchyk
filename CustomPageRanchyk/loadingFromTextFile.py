import numpy
import txtPreProcessing

def getMatrixAndDictionary(theme):
    return createSparse(theme), getDictionary(theme)


def getAmount(theme):
    path = txtPreProcessing.getFilePath("/data/text/" + theme + "/", "amount")
    with open(path) as amountFile:
        return int(amountFile.readline())


def getDictionary(theme):
    path = txtPreProcessing.getFilePath("/data/text/" + theme + "/", "nodes")
    with open(path + "lineFree") as file:
        index_map = dict()
        while True:
            inString = file.readline()
            if not inString.strip(): break
            key = inString.split()[0]
            file.readline()
            value = file.readline()
            file.readline()
            index_map[key] = value
    return index_map


def createSparse(theme):
    path = txtPreProcessing.getFilePath("/data/text/" + theme + "/", "adj_list")
    amount = getAmount(theme)
    matrix = numpy.zeros(shape=(amount, amount))
    with open(path) as file:
        for line in file:
            line = line.replace(":", "")
            values = line.split()[:-1]
            for i in range(1, len(values)):
                calc = 1/(len(values) - 1)
                matrix[int(values[i])][int(values[0])] = calc
    return matrix

