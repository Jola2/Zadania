import numpy as np

a = np.random.randint(low=1, high=100, size=24)
print(a)
b = a.reshape(4,3,2)
print(b)

# change the  shape of the previously created array  to two-dimensional
c = b.reshape(4,6)
print(c)

# create a vector containing consecutive natural numbers
d = np.array([1,2,3,4,5,6])

# overwrite array by adding this vector
print(d+c)

