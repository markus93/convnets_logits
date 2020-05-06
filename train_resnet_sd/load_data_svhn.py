# Loading Data - SVHN - followed paper (https://arxiv.org/pdf/1603.09382.pdf)

# Imports
import numpy as np
import scipy.io
from sklearn.model_selection import train_test_split
from os import path

PATH_DATA = path.join("..", "..", "data", "data_svhn")

# Split train data into train and validation gettting certain number of labels from each class
def train_val_split_count(x_train, y_train, size, seed):
    
    if seed != None:
        np.random.seed(seed)  # Set seed if it is stated.

    labels = set(y_train.flatten())  # Get label names
    n_labels = len(labels)  # Get number of labels

    x_val = []
    y_val = []
    split = []

    
    for i in labels:
        labels_i = np.where(y_train == i)[0]  # Take set of only one label
        samples = np.random.choice(labels_i, size)  # TODO: Check if enough labels in the class
        split.append(samples)

    split = np.array(split).flatten()
    #print(split[:10])

    x_val = np.array(x_train[split])
    y_val = np.array(y_train[split])
    
    x_train = np.delete(x_train, split, axis=0)
    y_train = np.delete(y_train, split, axis=0)
    
    return (x_train, x_val, y_train, y_val)

    
 



def load_data_svhn(seed = None):
    

    # Load in MatLab matrices
    test_mat = scipy.io.loadmat(path.join(PATH_DATA, 'test_32x32.mat'))
    train_mat = scipy.io.loadmat(path.join(PATH_DATA, 'train_32x32.mat'))
    extra_mat = scipy.io.loadmat(path.join(PATH_DATA, 'extra_32x32.mat'))


    # Get data from matrices
    x_test = test_mat.get('X')  #numpy arrays
    y_test = test_mat.get('y')

    x_train = train_mat.get('X')
    y_train = train_mat.get('y')

    x_extra = extra_mat.get('X')
    y_extra = extra_mat.get('y')
    
    
    

    # Reshape the matrices

    # [h,w,channels,samples] -> [samples,h,w,channels]
    
    x_test = np.transpose(x_test, axes=(3,0,1,2))
    x_train = np.transpose(x_train, axes=(3,0,1,2))
    x_extra = np.transpose(x_extra, axes=(3,0,1,2))
    
    x = np.concatenate([x_test, x_train])
    y = np.concatenate([y_test, y_train])
    
    test_size = len(y_test)
    
    print("Test_size:", test_size)
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=seed)  # random_state = seed



    # Split DATA
    x_train1, x_val1, y_train1, y_val1 = train_val_split_count(x_train, y_train, size = 400, seed = seed)  # 400 elements from each class
    x_extra2, x_val2, y_extra2, y_val2 = train_val_split_count(x_extra, y_extra, size = 200, seed = seed)


    # Add together train and extra data

    x_train_all = np.concatenate([x_train1, x_extra2])
    y_train_all = np.concatenate([y_train1, y_extra2])
    
    y_train_all -= 1  # So 0 would be smallest label and 9 biggest.
    #NB! Note that this way the labels are not actually correct, because 10 indicates the 0, FIX this.

    x_val_all = np.concatenate([x_val1, x_val2])
    y_val_all = np.concatenate([y_val1, y_val2])
    
    y_val_all -= 1  # So 0 would be smallest label and 9 biggest
    y_test -= 1  # So 0 would be smallest label and 9 biggest


    return ((x_train_all, y_train_all), (x_val_all, y_val_all), (x_test, y_test))



