import matplotlib.pyplot as plt
import numpy as np

grupa1 = (0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0)
print('Dane dot. grupy1')
print(len(grupa1))
print('Kobiety:', grupa1.count(0))
print('Kobiety:', grupa1.count(1))


grupa2 = (1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1)
print('Dane dot. grupy2')
print(len(grupa2))
print('Kobiety:', grupa2.count(0))
print('Kobiety:', grupa2.count(1))

grupa3 = (1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1)
print('Dane dot. grupy3')
print(len(grupa3))
print('Kobiety:', grupa3.count(0))
print('Kobiety:', grupa3.count(1))

x = list(zip(['grupa1', 'grupa1', 'grupa2', 'grupa2', 'grupa3', 'grupa3'],
             ['kobieta', 'mężczyzna', 'kobieta', 'mężczyzna', 'kobieta', 'mężczyzna']))
print(x)

plt.bar(['grupa1', 'grupa1', 'grupa2', 'grupa2', 'grupa3', 'grupa3'],
        ['kobieta', 'mężczyzna', 'kobieta', 'mężczyzna', 'kobieta', 'mężczyzna'],
        s=np.array([grupa1.count(0), grupa1.count(1), grupa2.count(0), grupa2.count(1), grupa3.count(0), grupa3.count(1)]))

plt.xlabel('Grupy osób zdających egzamin')
plt.ylabel('Płeć')
plt.title('Podział zdających  ze względu na płeć')
plt.legend(loc ='lower left')
plt.show()
