import numpy as np, pickle
from bz2 import BZ2File
from datetime import datetime
from pprint import pprint
from time import sleep
from tqdm import tqdm
from tqdm import tqdm_notebook
from scipy import sparse
import os
from sklearn.decomposition import randomized_svd
from sklearn.externals.joblib import Memory
import dataLoader
import adjacencyConstruction

PATH = '/data/dpedia/'
URL_BASE = 'http://downloads.dbpedia.org/3.5.1/en/'
filenames = ["redirects_en.nt.bz2", "page_links_en.nt.bz2"]

redirects_filename = dataLoader.getFilePath(PATH, filenames[0]);
page_links_filename = dataLoader.getFilePath(PATH, filenames[1]);

redirects = adjacencyConstruction.get_redirects(redirects_filename)

for i in range(10):
    print(redirects[i])
