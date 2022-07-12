import numpy as np


def main():
    numbers = np.arange(1, 30)
    a = np.random.choice(numbers, size=20, replace=False)
    print(a)

    # drawing 10 numbers from the object a with repetition
    print("with repetition", np.random.choice(a, size=10, replace=True))

    # drawing 10 numbers from the object a without repetition
    print("without repetition", np.random.choice(a, size=10, replace=False))

if __name__ == "__main__":
    main()
