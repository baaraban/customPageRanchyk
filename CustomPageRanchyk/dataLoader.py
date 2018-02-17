import os
from urllib.request import urlopen


def loadDataset(url, path, file_names):
    for filename in file_names:
        pathToLook = getFilePath(path, filename)
        if not os.path.exists(pathToLook):
            print("Downloading '%s', please wait..." % filename)
            os.write(os.open(pathToLook, os.O_RDWR | os.O_CREAT), (urlopen(url + filename).read()))


def getFilePath(path, file_name): return os.path.dirname(__file__) + path + file_name
