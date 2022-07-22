import pandas as pd


# create a column to show the word name of the grade
def slownie(marks):
    dictionary = {1.0: 'niedostateczny', 1.5: 'ponad niedostateczny', 2.0: 'dopuszczający',
                  2.5: 'ponad dopuszczający', 3.0: 'dostateczny', 3.5: 'ponad dostateczny',
                  4.0: 'dobry', 4.5: 'ponad dobry', 5.0: 'bardzo dobry', 5.5: 'ponad bardzo dobry',
                  6.0: 'celujący'}
    return dictionary[marks]


def main():
    marks = pd.read_excel('c:/Users/admin/Desktop/Dane_do_Pandas/dane_zad_1.xlsx', sheet_name='Oceny',
                          header=1, nrows=15, usecols=['Lp.', 'Imie', 'Nazwisko', 'Ocena'], index_col='Lp.')

    marks['slownie'] = marks['Ocena'].apply(slownie)
    print(marks)

    # create a column with information on whether the person is qualified ( grade 3 or higher)
    marks['Kwalfikacja'] = marks['Ocena'] >= 3

    # remove unqualified persons from the table
    marks.drop(marks[(marks['Kwalfikacja'] is False)].index, inplace=True)
    print(marks)


if __name__ == "__main__":
    main()
