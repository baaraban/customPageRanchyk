import os

DATA_PATH = "/data/text/"

USELESS_FILES = ["inv_adj_list"]

def getFilePath(path, file_name): return os.path.dirname(__file__) + path + file_name


def createWithoutBlankLines(path):
    with open(path, 'r') as infile, open(path + "lineFree", 'w') as outfile:
        infile.readline()
        for line in infile:
            if not line.strip(): continue
            outfile.write(line)


def createAmountFile(initialPath, amountPath):
    with open(initialPath, 'r') as infile, open(amountPath, 'w') as amountFile:
        amountFile.write(infile.readline())


def deleteUseless(directory, filenamesToDelete):
    for file in filenamesToDelete:
        if(os._exists(directory + file)):
            os.unlink(directory + file)


for name in os.listdir(getFilePath(DATA_PATH, "")):
    try:
        createAmountFile(getFilePath(DATA_PATH + name + '/', "nodes"), getFilePath(DATA_PATH + name + '/', "amount"))
        createWithoutBlankLines(getFilePath(DATA_PATH + name + '/', "nodes"))
        deleteUseless(getFilePath(DATA_PATH + name + '/', ''), USELESS_FILES)
    except UnicodeDecodeError:
        continue

