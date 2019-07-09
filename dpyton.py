import numpy as np
 
def display(matrix):
    print(matrix)
    #print("determinant: " + str(np.linalg.det(matrix)))
    print(np.linalg.eigvals(matrix))
    print("polynomial " + str(np.poly(matrix)))
    print("product " + str(product(matrix)))


#6 has nice eigenvalues--7 and 8 dont
def graph_laplacian(n):
    grap_lap = None
    if (n > 4):
        grap_lap = np.array([[0]*n]*n)
        for i in range(n):
            grap_lap[i,i] = 4
            grap_lap[i,(i-1)%n] = -1
            grap_lap[i,(i-2)%n] = -1
            grap_lap[i,(i+1)%n] = -1
            grap_lap[i,(i+2)%n] = -1
    else: 
        grap_lap = np.array([[-1] * n] * n)
        for i in range(n):
            grap_lap[i, i] = n - 1
    print("size: " + str(n))
    display(grap_lap)
    return grap_lap

def cycle(n):
    laplacian = np.array([[0] * n] * n)
    if (n == 2):
        for i in range(n):
            laplacian[i, i] = 1
            laplacian[i, (i - 1) % n ] = -1
    elif (n > 2):
        for i in range(n):
            laplacian[i, i] = 2
            laplacian[i, (i - 1) % n] = -1
            laplacian[i, (i + 1) % n] = -1
    
    print("size " + str(n))
    display(laplacian)
    return laplacian

def product(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    product = 1
    for e in eigenvalues:
        if (abs(e) >= 10 ** (-10)):
            product *= e
    return product / len(eigenvalues)


for i in range(1, 8):
    cycle(i)
