import matplotlib.pyplot as plt
import numpy as np

# create a scatterplot with points 1-10 on the x-axis and random integers 1-20 on the y-axis
def main():
    fig, ax = plt.subplots(figsize=(12, 6))
    rng = np.random.RandomState(200)
    colormap = rng.rand(10)
    ax.scatter(np.arange(1, 11, 1), np.random.randint(0, 20, 10), c=colormap, s=150, marker='D')
    ax.set_xticks(np.arange(0, 11, 1))
    plt.xlabel('Space 1', fontsize=14, fontweight='bold')
    plt.ylabel('Space 2', fontsize=14, fontweight='bold')
    plt.title('Diamonds', fontsize=18, fontweight='bold')
    plt.show()

if __name__ == "__main__":
    main()
