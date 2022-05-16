import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-8, 8, 20)
y = x ** 3
fig = plt.figure(figsize=(10, 5), facecolor='#0097a7')
ax = fig.add_axes((0.1, 0.1, 0.7, 0.7), facecolor='#b3e5fc')
ax.plot(x, y, color='k', linestyle = 'dashdot', marker='p', linewidth=2, label= r'funkcja  $x^3$')
ax.set_yticks(np.arange(-401, 401, 200))
ax.set_yticklabels(labels=['- czterysta','- dwieście','zero', 'dwieście', 'czterysta'])
ax.set_title(r'Wykres funkcji $x^3$', fontdict={'fontsize': 18, 'color': '#c4c4c4'})
ax.legend()
ax.grid()
plt.show()
