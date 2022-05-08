import numpy as np
def matrix(n):
    arr = np.zeros((n,n))
    for k in range(n):
        arr[np.arange(n-k), np.arange(n-k) + k]= k + 1
    return arr

print(matrix(8))