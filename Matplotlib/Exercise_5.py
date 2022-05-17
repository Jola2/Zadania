import matplotlib.pyplot as plt
import numpy as np

grupa_1 = (21, 41, 22, 41, 42, 48, 20, 21, 20, 40, 40, 34, 21, 41, 47, 39, 43, 47, 28, 35, 49, 47, 22, 33, 30, 22, 29, 30, 41, 42)
grupa_2 = (47, 49, 41, 31, 45, 24, 29, 22, 28, 24, 36, 28, 49, 40, 39, 39, 49, 26, 45, 26, 32, 30, 30, 41, 33)
grupa_3 = (27, 44, 27, 40, 39, 42, 27, 28, 20, 30, 44, 38, 26, 37, 37, 27, 28, 30, 43, 37, 39, 26, 38, 47, 45, 40, 35)

srednia_1 = sum(grupa_1)/len(grupa_1)
print('Średnia grupy_1:', srednia_1)
print(min(grupa_1))
print(max(grupa_1))

srednia_2 = sum(grupa_2)/len(grupa_2)
print('Średnia grupy_2:', srednia_2)
print(min(grupa_2))
print(max(grupa_2))

srednia_3 = sum(grupa_3)/len(grupa_3)
print('Średnia grupy_3:', srednia_3)
print(min(grupa_3))
print(max(grupa_3))

srednia_grup = (srednia_1, srednia_2, srednia_3)
min_grup = (20, 22, 20)
max_grup = (49, 49, 47)
x = np.arange(3)
plt.figure(figsize=(15,6))

plt.bar(x, srednia_grup, width =0.3)
plt.ylabel ('Punkty')
plt.title ( 'Srednia liczba punktow w grupach')
plt.xticks (x , ('Grupa 1', 'Grupa 2', 'Grupa 3') )
plt.yticks ( np.arange (0 , 35 , 10))
plt.show()
