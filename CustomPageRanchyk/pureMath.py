import numpy as np

def checkIfDependent(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            if i != j:
                inner_product = np.inner(
                    matrix[i,:],
                    matrix[j,:]
                )
                norm_i = np.linalg.norm(matrix[i,:])
                norm_j = np.linalg.norm(matrix[j,:])
                print('i: ', i)
                print('j: ', j)
                print ('I: ', matrix[i,:])
                print ('J: ', matrix[j,:])
                print ('Prod: ', inner_product)
                print ('Norm i: ', norm_i)
                print ('Norm j: ', norm_j)
                if np.abs(inner_product - norm_j * norm_i) < 1E-5:
                    print('Dependent')
                else:
                    print('Independent')