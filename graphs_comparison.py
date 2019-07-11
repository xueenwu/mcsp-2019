import numpy as np
 

def graph_laplacian_connected(k,n):
    grap_lap = None
    if (n > 2*k):
        grap_lap = np.array([[0]*n]*n)
        for i in range(n):
            grap_lap[i,i] = 2*k
	    for j in range(1,k+1):
                grap_lap[i,(i-j)%n] = -1
                grap_lap[i,(i+j)%n] = -1      
    #print("connected to the previous and next " + str(k) + " things")
    #print("size: " + str(n))
    #print(grap_lap)
    #print("determinant: " + str(np.linalg.det(grap_lap)))
    #print(np.linalg.eigvals(grap_lap))
    #print("polynomial " + str(np.poly(grap_lap)))
    #print("product " + str(product(grap_lap)))
    return grap_lap

def graph_laplacian_disconnected(k,n):
    grap_lap = None
    if (n > 2*k):
        grap_lap = np.array([[0]*n]*n)
        for i in range(n):
            grap_lap[i,i] = 2*k
	    for j in range(1,k+1):
                if (i-j > -1):                
		    grap_lap[i,(i-j)] = -1
                if (i+j < n):
		    grap_lap[i,(i+j)] = -1 
	    if (i < k):
		grap_lap[i,i] = k+i
	    if (i > n-k-1):
		grap_lap[i,i] = k+n-1-i
		
     
    #print("connected to the previous and next " + str(k) + " things")
    #print("size: " + str(n))
    #print(grap_lap)
    #print("determinant: " + str(np.linalg.det(grap_lap)))
    #print(np.linalg.eigvals(grap_lap))
    #print("polynomial " + str(np.poly(grap_lap)))
    #print("product " + str(product(grap_lap)))
    return grap_lap

def product(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    product = 1
    for e in eigenvalues:
        if (abs(e) >= 10 ** (-10)):
            product *= e
    return product / len(eigenvalues)

def comparison(k):
    ratiolist = []
    for n in range(2k+1,25):
        comp = float(product(graph_laplacian_connected(k,n)))/float(n*product(graph_laplacian_disconnected(k,n))) 
        ratiolist.append(comp)
    return ratiolist

for k in range(1,9):
    print(comparison(k))
    
    


