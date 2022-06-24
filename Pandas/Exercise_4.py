import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read csv
df = pd.read_csv('c:/Users/admin/Desktop/Dane_do_Pandas/wig_paliwa_m.csv',parse_dates =["Date"], index_col ='Date')

# create a summary  for each year
df.reset_index(inplace=True)
summary = df.groupby(pd.Grouper(key='Date', freq='Y')).describe().T
print(summary)

# select the maximum values of the variable close from the created table and show on  a two graph: line and bar
df = summary.loc[('Close', 'max')]
df.plot(figsize=(20, 5), title ='Maximum values of the variable Close in  1991-2022')
plt.show()

plt.figure(figsize=(15,6), )
x = [f'Rok {i}' for i in list(range(1991, 2023))]
y = summary.loc[('Close', 'max')]
plt.barh(x, y , orientation='horizontal')
plt.title('Maximum values of the variable Close in  1991-2022')
plt.show()

# convert monthly data to annual data
df = pd.read_csv('c:/Users/admin/Desktop/Dane_do_Pandas/wig_paliwa_m.csv',parse_dates =["Date"], index_col ='Date')
df.reset_index(inplace=True)
annual_data = df.groupby(pd.Grouper(key='Date', freq='Y')).sum()
print(annual_data)
# tutaj jeszcze muszę rozpracować dlaczego w Pycharmie występuję błąd, a w Jupyterze działa poprawnie
# jak jeszcze raz wczytam csv to działa - tylko nie wiem czy dwukrotne wczytanie tego samego pliku jest dozwolone

# create a summary with 3 tables and save all 3 tables to a common Excel
writer = pd.ExcelWriter('paliwa.xlsx')
df.to_excel(writer, 'label_1')
summary.to_excel(writer, 'label_2')
annual_data.to_excel(writer, 'label_3')

writer.save()

