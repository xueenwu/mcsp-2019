import numpy as np
 
#6 has nice eigenvalues--7 and 8 dont
def eigenstuff(n):
    grap_lap = np.array([[0]*n]*n)
    for i in range(n):
        grap_lap[i,i] = 4
        grap_lap[i,(i-1)%n] = -1
        grap_lap[i,(i-2)%n] = -1
        grap_lap[i,(i+1)%n] = -1
        grap_lap[i,(i+2)%n] = -1
    print("size: " + str(n))
#    print(grap_lap)
    #print("determinant: " + str(np.linalg.det(grap_lap)))
    #print(np.linalg.eigvals(grap_lap))
    print("product " + str(product(grap_lap)))
    return grap_lap

def product(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    product = 1
    for e in eigenvalues:
        if (e != 0):
            product *= e
    return product / len(eigenvalues)


for i in range(1, 9):
    eigenstuff(i)

