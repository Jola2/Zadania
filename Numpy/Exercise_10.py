import numpy as np
def matrix(n):
    arr = np.zeros((n,n))
    arr[np.arange(n), np.arange(n)] = 1 # diagonal is 1 jeśli zrobię arr = np.identity(n) bo nie musze tego pisać
    arr[np.arange(n-1), np.arange(n-1) + 1]= 2
    arr[np.arange(n-2), np.arange(n-2) + 2] = 3
    arr[np.arange(n-3), np.arange(n-3) + 3] = 4
    arr[np.arange(n-4), np.arange(n-4) + 4] = 5
    return arr

print(matrix(5))

# nie wiem, jak zapisać w jednej linijce kodu, zeby działo niezalężnie od liczby n

n=5
A = np.zeros((n,n))
A += np.arange(n)
print(A)
# kombinowałam, żeby zapisać w podobny sposób, tylko nie wiem jak co zrobić z przekątnymi
