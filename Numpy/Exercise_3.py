import numpy as np

numbers = np.arange(1, 30)

# generate 20 random numbers between 1-30  draw with repetition
print("with repetition",np.random.choice(numbers, size=20, replace = True))

# generate 20 random numbers between 1-30  draw without repetition
print("without repetition",np.random.choice(numbers, size=20, replace = False))

