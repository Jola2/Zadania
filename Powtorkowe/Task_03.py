import collections
import numpy as np


# find the probability of occurrence each letter in the text
def probability(txt):
    return dict((i, txt.count(i)/len(txt)) for i in txt)


def main():
    file = open('c:/Users/admin/Desktop/Dane_do_zadan/litery.txt', 'r')
    file = file.read()
    print('Probability of letters occurring', probability(file))

    # selecting pairs of letters
    a = [f'{file[0+i:2+i]}' for i in range(len(file))]
    a = a[:-1]

    # counting the number of occurrences of letters pairs and their probabilities
    dictionary = collections.Counter(a)
    list_of_letters = ['e', 'f', 'h', 'z']
    probability_list = []
    for letter in list_of_letters:
        grouping_letters = [(key, value) for key, value in dictionary.items() if key.startswith(letter)]
        grouping_letters.sort()
        list_of_value = [value[1] for value in grouping_letters]
        probability_for_group = [x / sum(list_of_value) for x in list_of_value]
        probability_list.append(probability_for_group)
    print('Transition matrix')
    c = np.array(probability_list)
    print(c)


if __name__ == '__main__':
    main()
