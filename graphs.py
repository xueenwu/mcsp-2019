import numpy as np
 

def graph_laplacian(k,n):
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

def product(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    product = 1
    for e in eigenvalues:
        if (abs(e) >= 10 ** (-10)):
            product *= e
    return product / len(eigenvalues)

arrayofstuff = np.array([[0]*21]*6)
#x = product(graph_laplacian(1, 3))
#print(x)
#arrayofstuff[1, 3] = product(graph_laplacian(1, 3))
#print(arrayofstuff)
#arrayofstuff[1, 3] = x
#print(arrayofstuff)
#print(product(graph_laplacian(1,3)))
for a in range(1,21):
    for b in range(1,6):
        if (a > 2*b):
            arrayofstuff[b,a] = int(product(graph_laplacian(b,a)) + 0.5)

print(arrayofstuff)



	
