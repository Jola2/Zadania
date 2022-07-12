import matplotlib.pyplot as plt
import numpy as np

# find a way to prevent x-ticks from overlapping title
def main():
    ncols, nrows = 3, 3
    fig, axes = plt.subplots(nrows, ncols, figsize=(12, 8))

    for m in range(nrows):
        for n in range(ncols):
            axes[m, n].plot(np.arange(50), np.random.normal(0, 5, size=50))
            axes[m, n].set_title(f"axes[{m}, {n}]")

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
