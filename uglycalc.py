import numpy as np

def laurent(k):
    coefs_array = np.array([1]*(2*k+1))
    coefs_array[k] = -2*k
    return np.roots(coefs_array)
def bigroots(k):
    absvals = np.absolute(laurent(k))
    roots = []
    for i in range(2*k-1):
        if (absvals[i] >= 1):
            roots.append(absvals[i])
    return np.poly(roots)
        
for k in range(1,10):
    print(bigroots(k))
    
    
 

