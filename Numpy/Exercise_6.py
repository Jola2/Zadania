import numpy as np

a = np.random.randint(low=1, high=100, size=24)
print(a)
b = a.reshape(4,3,2)
print(b)
c = b.reshape(4,6)
print(c)
d = np.array([1,2,3,4,5,6])
print(d+c)

