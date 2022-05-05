import numpy as np


numbers = np.arange(1, 30)
print("z powtórzeniami",np.random.choice(numbers, size=20, replace = True))
print("bez powtórzeń",np.random.choice(numbers, size=20, replace = False))

#print(np.random.randint(low=1, high=30, size=20))
#zastanawiam się, który sposób do wygenerowania jest lepszy/poprawny  i jaki powinnam używać: random.choice czy random.randint? 
#W przypadku random.randint jest większy problem z generowaniem bez powtórzeń, bo nie mogę użyć replace = False i musiałabym bardziej pokombinować
