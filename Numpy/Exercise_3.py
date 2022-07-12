import numpy as np

def main():
    numbers = np.arange(1, 30)

    # generate 20 random numbers between 1-30  draw with repetition
    a=np.random.choice(numbers, size=20, replace=True)
    print("with repetition", a)

    # generate 20 random numbers between 1-30  draw without repetition
    b=np.random.choice(numbers, size=20, replace=False)
    print("without repetition", b)

if __name__ == "__main__":
    main()