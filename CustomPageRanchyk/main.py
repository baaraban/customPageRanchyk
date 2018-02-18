import numpy as np, pickle
from bz2 import BZ2File
from datetime import datetime

import loadingFromTextFile
import pureMath
import calculations
import numpy

matrix, dict = loadingFromTextFile.getMatrixAndDictionary("armstrong")

test = numpy.ones(shape=(3,3))
test[0][0] = 0;
test[0][1] = 0.5;
test[0][2] = 0;
test[1][0] = 0.5;
test[1][1] = 0.5;
test[1][2] = 0;
test[2][0] = 0.5;
test[2][1] = 0;
test[2][2] = 0;
print(test);

result = calculations.powerRankMethod(calculations.calculateMMatrix(test))
print(result)




