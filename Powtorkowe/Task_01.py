import numpy as np


def main():
    a = np.array([3, 42, 2, 71, 2, 3, 17, 4, 1, 32, 1, 4, 84, 1, 4, 91, 1, 1, 1, 83])
    a = np.select([a > 70, a < 15], [70, 15], a)
    print(a)


if __name__ == "__main__":
    main()
