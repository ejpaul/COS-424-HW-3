'''
Created on April 17, 2015

@author: epaul626

Utility function for constructing sparse binary matrix 
from test data set
'''
import numpy as np
from scipy.sparse import csc_matrix
import os, sys

# Returns numpy CSC binary matrix of train data
# given path  
def to_binary(file):
	ad1 = np.loadtxt(file, usecols=(0,))
	ad2 = np.loadtxt(file, usecols=(1,))
	data = np.ones((len(ad1),))
	return csc_matrix((data, (ad1, ad2)), shape=(len(ad1), len(ad1)))

def to_csc(file):
	ad1 = np.loadtxt(file, usecols=(0,))
        ad2 = np.loadtxt(file, usecols=(1,))
        data = np.loadtxt(file, usecols=(2,))
        return csc_matrix((data, (ad1, ad2)), shape=(len(ad1), len(ad1)))

def main(argv):
	dir = '/u/biancad/COS424/bitcoin'
	train = 'txTripletsCounts.txt'
	os.chdir(dir)
	binary = to_binary(train)
	print binary

	csc = to_csc(train)
	print csc

if __name__ == '__main__':
    main(sys.argv[1:])
