import numpy as np
from scipy.sparse import linalg
import pylab as P
import os, sys
sys.path.append('../utils/')
from binary import *

def main(argv):
        dir = '.'
        train = 'txTripletsCounts.txt'
        os.chdir(dir)
        binary = to_binary(train)

	svd = linalg.svds(binary, 25, tol=1e-10)
	P.plot(svd)
	P.show()
	 
if __name__ == '__main__':
    main(sys.argv[1:])
