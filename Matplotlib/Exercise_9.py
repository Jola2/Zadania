import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-2 * math.pi, 2 * math.pi, 80)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = 1.0 / np.tan(x)

figure, axis = plt.subplots(2, 2, figsize=(12, 8))
figure.suptitle('Funkcje trygonometryczne', fontsize=24)

axis[0, 0].plot(x, y1, color='k', linestyle='solid', label='Sinus')
axis[0, 0].set_title(r"Wykres funkcji $\sin (\alpha$)", fontdict={'fontsize': 10})
rect = axis[0, 0].patch
rect.set_facecolor('#b2dfdb')

axis[0, 1].plot(x, y2, color='k', linestyle='dashdot', label='Cosinus')
axis[0, 1].set_title(r"Wykres funkcji $\cos (\alpha$)", fontdict={'fontsize': 10})
rect = axis[0, 1].patch
rect.set_facecolor('#4db6ac')

axis[1, 0].plot(x, y3, color='k', linestyle='dashed', label='Tangens')
axis[1, 0].set_title(r"Wykres funkcji $\tan(\alpha$)", fontdict={'fontsize': 10})
axis[1, 0].set_yticks([-25, 0, 25, 50])
rect = axis[1, 0].patch
rect.set_facecolor('#a7ffeb')

axis[1, 1].plot(x, y4, color='k', linestyle='dotted', label='Cotangens')
axis[1, 1].set_title(r"Wykres funkcji $\cot\alpha$)", fontdict={'fontsize': 10})
axis[1, 1].set_yticks([-1])
rect = axis[1, 1].patch
rect.set_facecolor('#64b5f6')

leg = figure.legend(loc='lower right')
plt.show()
