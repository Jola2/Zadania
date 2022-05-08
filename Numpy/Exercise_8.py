import numpy as np
from collections import Counter

arr = [1,2,3,3,3,3,2]
dictionary = Counter(arr)
print(dictionary)


for key in dictionary:
    print('Prawdopodobieństwo wystąpienie',key,'wynosi',dictionary[key]/len(arr))