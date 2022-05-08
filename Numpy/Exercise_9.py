import numpy as np

a = np.ones((9, 9), int)
np.fill_diagonal(a, [2,3,4,5,6,7,8,9,10])
print(a)


