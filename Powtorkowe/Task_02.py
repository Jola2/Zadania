# find the probability of occurrence each number from arr
def probability(arr):
    return dict((i, arr.count(i)/len(arr)) for i in arr)


def main():
    a = probability([1, 2, 3, 3, 3, 3, 2, 4, 5, 4])
    print(a)


if __name__ == "__main__":
    main()
