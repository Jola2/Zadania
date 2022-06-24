import numpy as np
from collections import Counter

# find the probability of occurrence each number from arr
arr = [1,2,3,3,3,3,2]
dictionary = Counter(arr)
print(dictionary)


for key in dictionary:
    print('Probability of occurrence',key,'is',dictionary[key]/len(arr))