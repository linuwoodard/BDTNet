### functions written to support the main code

import scipy.io as sio
import numpy as np
import os

def load_data(data_path):
    '''
    inputs: 
        data_path: path to the data file

    outputs:
        mechFreq: mechanical frequencies
        optFreq: optical frequencies
        mechQ: mechanical Qs
        optQ: optical Qs
        paramsMat: parameters matrix
    '''
    if not os.path.exists(data_path):
        print("File not found")
        return
    print("Loading data from: ", data_path, "\n")
    data = sio.loadmat(data_path)
    mechFreq = data['mechFreqMat']
    optFreq = data['optFreqMat']
    mechQ = data['mechQMat']
    optQ = data['optQsMat']
    paramsMat = data['paramsMat']
    return mechFreq, optFreq, mechQ, optQ, paramsMat

