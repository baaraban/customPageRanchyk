import os
import numpy
import txtPreProcessing;

def getFilePath(path, file_name): return os.path.dirname(__file__) + path + file_name

def getTextDictionary(theme):
    path = getFilePath("/data/text/" + theme + "/", "nodes")
    #txtPreProcessing.createWithoutBlankLines(path)
    with open(path + "lineFree") as file:
        amount = int(file.readline())
        matrix = createSparse(theme, amount)
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

def createSparse(theme, amount):
    path = getFilePath("/data/text/" + theme + "/", "adj_list")
    matrix = numpy.zeros(shape=(amount, amount))
    with open(path) as file:
        for line in file:
            line = line.replace(":", "")
            values = line.split()[:-1]
            for i in range(1, len(values)):
                calc = 1/(len(values) - 1)
                matrix[int(values[0])][int(values[i])] = calc

    for i in range(amount):
        if(matrix[2][i] != 0):
            print (matrix[2][i], "   ", i)


getTextDictionary("armstrong")


