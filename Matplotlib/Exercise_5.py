import matplotlib.pyplot as plt
import numpy as np

# calculate the mean of each group and create a bar graph comparing the results
def main():
    group_1 = (
    21, 41, 22, 41, 42, 48, 20, 21, 20, 40, 40, 34, 21, 41, 47, 39, 43, 47, 28, 35, 49, 47, 22, 33, 30, 22, 29, 30, 41,
    42)
    group_2 = (47, 49, 41, 31, 45, 24, 29, 22, 28, 24, 36, 28, 49, 40, 39, 39, 49, 26, 45, 26, 32, 30, 30, 41, 33)
    group_3 = (
    27, 44, 27, 40, 39, 42, 27, 28, 20, 30, 44, 38, 26, 37, 37, 27, 28, 30, 43, 37, 39, 26, 38, 47, 45, 40, 35)

    avg_1 = sum(group_1) / len(group_1)
    avg_2 = sum(group_2) / len(group_2)
    avg_3 = sum(group_3) / len(group_3)

    avg_of_groups = (avg_1, avg_2, avg_3)
    min_groups = (min(group_1), min(group_2), min(group_3))
    max_groups = (max(group_1), max(group_2), max(group_3))
    range_of_plot = [(max(group_1) - min(group_1)) / 2, (max(group_2) - min(group_2)) / 2,
                     (max(group_3) - min(group_3)) / 2]

    x = np.arange(3)
    plt.figure(figsize=(15, 6))
    plt.bar(x, avg_of_groups, width=0.3, yerr=range_of_plot, capsize=6)
    plt.ylabel('Points')
    plt.title('The average number of points depending on groups')
    plt.xticks(x, ('Group 1', 'Group 2', 'Group 3'))
    plt.yticks(np.arange(0, 52, 3))
    plt.show()

if __name__ == "__main__":
    main()