import numpy as np


numbers = np.arange(1, 30)
print("z powtórzeniami",np.random.choice(numbers, size=20, replace = True))
print("bez powtórzeń",np.random.choice(numbers, size=20, replace = False))

