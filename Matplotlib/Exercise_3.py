
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 20)
y1 = x
y2 = x ** 2


fig, ax = plt.subplots(figsize=(8,5))
ax.plot(x, y1, color='k')
ax.plot(x, y2, color='k')
ax.fill_between(x, y1, y2, color='#64ffda')
ax.annotate(r'Pole figury stworzonej przez przecięcie krzywych $𝑦=𝑥$ i $𝑦=𝑥^2$',
            xy=(0.4, 0.4), xycoords='data',
            xytext=(-0.02, 0.8),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',verticalalignment='top')
plt.show()
