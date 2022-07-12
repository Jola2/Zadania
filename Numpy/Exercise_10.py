import numpy as np

# write a function that takes one argument  with natural number(n)
# and generate a matrix of dimensions n x n such that below the main diagonal  has all 0,
# on the main diagonal has 1,on the second diagonal has 2, etc.

def matrix(n):
    arr = np.zeros((n,n))
    for k in range(n):
        arr[np.arange(n-k), np.arange(n-k) + k]= k + 1
    return arr

def main():
    a = matrix(8)
    print(a)

if __name__ == "__main__":
    main()
