import numpy as np

# generate a matrix that contains numbers from 2 to 10 on the main diagonal and number 1 everywhere else
a = np.ones((9, 9), int)
np.fill_diagonal(a, [2,3,4,5,6,7,8,9,10])
print(a)


