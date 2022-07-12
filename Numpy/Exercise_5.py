import numpy as np

# create a matrix with the shape of (4,3,2)
def main():
    arr = np.random.randint(low=1, high=100, size=24)
    print(arr)
    print(arr.reshape(4, 3, 2))

    print('Second way')
    np.random.seed(0)
    arr = np.random.rand(4, 3, 2)
    print(arr)
    arr *= 100
    print(arr.round())

if __name__ == "__main__":
    main()
