import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(figsize=(12,6))
rng = np.random.RandomState(200)
colormap = rng.rand(10)
ax.scatter(np.arange(1, 11, 1), np.random.randint(0, 20, 10), c=colormap ,s=150, marker='D')
ax.set_xticks(np.arange(0, 11, 1))
plt.xlabel('Space 1', fontsize = 14, fontweight='bold')
plt.ylabel('Space 2', fontsize = 14, fontweight='bold')
plt.show()
