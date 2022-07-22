import numpy as np


# create a function that takes vectors and changes each vector to be the length of the longest of them.
def connection(arr):
    longest = arr[sorted([(i, len(l)) for i, l in enumerate(arr)], key=lambda t: t[1])[-1][0]]
    desired_len = len(longest)
    new_arr = []
    # fill artificially created places with zeros
    for item in arr:
        new_arr.append(np.pad(item, (0, desired_len-len(item))))
    return new_arr


def main():
    my_arr = connection([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 4, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]])
    print(*my_arr, sep=', ')


if __name__ == '__main__':
    main()
