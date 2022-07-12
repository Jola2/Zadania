
# find the probability of occurrence each number from arr
def probability(arr_):
    return dict((i, arr_.count(i)/len(arr_)) for i in arr_)


def main():
    a = probability([1,2,3,3,3,3,2])
    print(a)

if __name__ == "__main__":
    main()

