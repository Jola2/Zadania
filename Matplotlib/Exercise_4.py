import matplotlib.pyplot as plt
import numpy as np

# create a graph of 50 lines x, 2x, 3x, ..., 50x
def main():
    fig, ax = plt.subplots(figsize=(12, 6))
    num_plots = 50
    colormap = plt.cm.gist_ncar
    plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, num_plots))))
    x = np.arange(51)
    labels = []
    for i in range(1, num_plots + 1):
        plt.plot(x, i * x)
        labels.append(r'$y = %i \bullet x $' % i)
    plt.legend(labels, ncol=5, loc='upper right',
               bbox_to_anchor=[0.4, 0.9],
               columnspacing=1.0, labelspacing=0.0,
               handletextpad=0.0, handlelength=0.5,
               fancybox=True, shadow=True, fontsize=7)
    plt.show()

if __name__ == "__main__":
    main()




