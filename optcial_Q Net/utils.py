### functions written to support the main code

import scipy.io as sio
import numpy as np
import os
import json

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


def write_json(data, path):
    '''
    saves python dictionary to a json file.
    Inputs:
        data: python dictionary
        path: path to save the json file

    Outputs:
        None
    '''
    print('Writing data to: ', path)
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)  # indent=4 for pretty printing


def read_json(path):
    '''
    reads json file and returns the data as python dictionary
    Inputs:
        path: path to the json file
    
    Outputs:
        data: python dictionary
    '''
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data