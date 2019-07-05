import numpy as np
n = 6
#6 has nice eigenvalues--7 and 8 dont
print("hello world")
grap_lap = np.array([[0]*n]*n)
for i in range(n):
  grap_lap[i,i] = 4
  grap_lap[i,(i-1)%n] = -1
  grap_lap[i,(i-2)%n] = -1
  grap_lap[i,(i+1)%n] = -1
  grap_lap[i,(i+2)%n] = -1
print(grap_lap)
print(np.linalg.eigvals(grap_lap))
