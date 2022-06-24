import numpy as np
import pandas as pd

marks = pd.read_excel('c:/Users/admin/Desktop/Dane_do_Pandas/dane_zad_1.xlsx', sheet_name='Oceny',
                      header=1, nrows=15, usecols=['Lp.', 'Imie', 'Nazwisko', 'Ocena'], index_col='Lp.')

# create a column to show the word name of the grade
def slownie(ocena):
  if ocena == 1.0:
    return "niedostateczny "
  elif ocena == 1.5:
    return "ponad niedostateczny"
  elif ocena == 2.0:
    return "dopuszczający"
  elif ocena == 2.5:
    return "ponad dopuszczający"
  elif ocena == 3.0:
    return "dostateczny "
  elif ocena == 3.5:
    return "ponad dostateczny "
  elif ocena == 4.0:
    return "dobry"
  elif ocena == 4.5:
    return "ponad dobry"
  elif ocena == 5.0:
    return "bardzo dobry"
  elif ocena == 5.5:
    return "ponad bardzo dobry"
  else:
    return "celujący"

# create a column with information on whether the person is qualified ( grade 3 or higher)
marks['Kwalfikacja'] = marks['Ocena'] >= 3

# remove unqualified persons from the table
marks.drop(marks[(marks['Kwalfikacja'] == False)].index, inplace=True)
print(marks)