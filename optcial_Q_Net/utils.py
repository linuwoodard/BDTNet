### functions written to support the main code

import scipy.io as sio
import numpy as np
import os
import json
import matplotlib.pyplot as plt

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


def show_predicted_Qs(example_numbers, batch_number, dataset, model):
    """
    given tensorflow dataset, model, and example numbers, this function prints the predicted Qs for the examples
    as well as the Qs from the dataset.

    Inputs:
        example_numbers: list of example numbers to be predicted
        batch_number: batch number to be predicted
        test_dataset: tensorflow dataset -- typically test dataset
        model: trained model

    Outputs:
        predicted, true
    """

    train_numbers = example_numbers


    test_iterator = iter(dataset)
    for batch in range(batch_number):
        # itterate to the batch of interest
        batch_X, batch_Y = next(test_iterator)
        

    predicted = []
    true = []
    for train_number in train_numbers:
        # Extract a single input and label pair from the batch
        # For example, take the first item from the batch
        single_input = batch_X[train_number].numpy()  # Convert to NumPy array
        single_label = batch_Y[train_number].numpy()  # Convert to NumPy array
        
        single_input =  np.expand_dims(single_input, axis=0) 
        
        prediction = model.predict(single_input, verbose = 0)

        predicted.append(10**(prediction[0][0]))
        true.append(10**(single_label[0]))

        print("predicted Q = {}".format(10**(prediction[0][0])))
        print("true Q = {}\n".format(10**(single_label[0])))

    return predicted, true


def show_train_test_dist(train_dataset, test_dataset):  
    """
    plots distribution of optical Qs for train and test datasets.
    Input datasets must be before batching.
    Inputs:
        train_data: type = tf.data.Dataset 
        test_data: type = tf.data.Dataset

    Outputs:
        train_optQ: np.array of optical Qs from training dataset
        test_optQ: np.array of optical Qs from testing dataset
    """

    # Extract optQ_linearized from train and test datasets
    train_optQ = [optQ for _, optQ in train_dataset]
    test_optQ = [optQ for _, optQ in test_dataset]
    ## let's actually look at our data breakup
    # Convert to NumPy arrays for histogram plotting
    train_optQ = np.array(train_optQ)
    test_optQ = np.array(test_optQ)

    # Plot histograms
    plt.figure(figsize=(8, 6))
    plt.subplot(1, 1, 1)
    plt.hist(train_optQ, bins=30, color='blue', alpha=0.7, label='Train Dataset')
    plt.title('Histogram of optQ_linearized - Train Dataset')
    plt.xlabel('optQ_linearized')
    plt.ylabel('Frequency')
    plt.legend()

    plt.subplot(1, 1, 1)
    plt.hist(test_optQ, bins=30, color='orange', alpha=0.7, label='Test Dataset')
    plt.title('Histogram of optQ_linearized - Test Dataset')
    plt.xlabel('optQ_linearized')
    plt.ylabel('Frequency')
    plt.legend()

    return train_optQ, test_optQ