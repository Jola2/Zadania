import numpy as np
import pandas as pd

# read xlsx and load a table that should contain 4 columns
def main():
    marks = pd.read_excel('c:/Users/admin/Desktop/Dane_do_Pandas/dane_zad_1.xlsx', sheet_name='Oceny',
                          header=1, nrows=15, usecols=['Lp.', 'Imie', 'Nazwisko', 'Ocena'], index_col='Lp.')
    print(marks)

if __name__ == "__main__":
    main()