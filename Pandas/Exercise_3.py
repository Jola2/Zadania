import calendar
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, date

def main():
    # read csv
    df = pd.read_csv('c:/Users/admin/Desktop/Dane_do_Pandas/weatherHistory.csv')

    # replace the 'Formatted Date' column with the column containing the datetime type
    df['Formatted Date'] = df['Formatted Date'].apply(lambda x: x[:19])
    df['Formatted Date'] = pd.to_datetime(df['Formatted Date'])
    print(df)

    # create a bar graph of the frequency of the top 5 weather information
    df['Summary'].value_counts().head()
    x = np.arange(5)
    y = df['Summary'].value_counts().head()
    plt.figure(figsize=(12, 5))
    plt.bar(x, y, width=0.5, align='center')
    plt.xticks(x, ['Partly Cloudy', 'Mostly Cloudy', 'Overcast ', 'Clear', 'Foggy'])
    plt.ylabel('Frequency', fontsize=16)
    plt.title('Five of the most popular weather information', fontsize=16)
    plt.show()

    # draw the average, minimum and maximum monthly temperatures across all years on a common graph
    temperature = df.resample('M', on='Formatted Date').agg(minimum=('Temperature (C)', 'min'),
                                                            maximum=('Temperature (C)', 'max'),
                                                            average=('Temperature (C)', 'mean'))
    temperature.plot(figsize=(20, 5), title='Temperature over the years')
    plt.show()

    # show the average weekly temperatures in June 2014-2016 in the bar chart
    june = df.resample('W', on='Formatted Date')['Temperature (C)'].mean()
    data_june_2014 = june[june.index.year.isin([2014]) & (june.index.month == 6)]
    data_june_2015 = june[june.index.year.isin([2015]) & (june.index.month == 6)]

    # fill the fifth week of June 2015 and 2016 as 0, because they are only 4 weeks
    filled_june_2015 = np.append(data_june_2015.values, 0)
    data_june_2016 = june[june.index.year.isin([2016]) & (june.index.month == 6)]
    filled_june_2016 = np.append(data_june_2016.values, 0)

    x = np.arange(5)
    y1 = data_june_2014.values
    y2 = filled_june_2015
    y3 = filled_june_2016
    plt.figure(figsize=(15, 5))
    width = 0.2
    plt.bar(x - width, y1, width, color='red')
    plt.bar(x, y2, width, color='green')
    plt.bar(x + width, y3, width, color='blue')

    plt.xticks(x, ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5'])
    plt.ylabel("Temperature")
    plt.legend(["2014", "2015", "2016"])
    plt.title('Average weekly temperatures in June 2014-2016', fontsize=12)
    plt.show()

    # create two sub-graphs  for 2006 - 2016  and show the change in mean temperature
    # the corresponding month (2006 - June, 2007-JUly, etc.) on the first sub-chart and the change
    #  of the maximum temperatures in June on the second.
    for x in range(1, 13):
        calendar.month_name[x]

    months = [6, 7, 8, 9, 10, 11, 12]
    for i in months:
        tem = df.resample('D', on='Formatted Date')['Temperature (C)'].mean()
        tem = tem.diff()
        plt.figure(figsize=(18, 3))
        czerwiec = tem[(tem.index.year == 2000 + i) & (tem.index.month == i)]
        czerwiec.plot(title=f'Change in the average temperature in {calendar.month_name[i]} {2000 + i}')
        plt.show()

        zmiany_max = df.resample('D', on='Formatted Date')['Temperature (C)'].max()
        zmiany_max = zmiany_max.diff()
        plt.figure(figsize=(18, 3))
        ddd = zmiany_max[(zmiany_max.index.year == 2000 + i) & (zmiany_max.index.month == 6)]
        ddd.plot(title=f'Change in maximum temperature in June {2000 + i}')

        plt.show()

    # show the average weekend temperature for each month in  2014-2016
    average = df.resample('D', on='Formatted Date')['Temperature (C)'].mean()
    data_weekend_2014 = average[average.index.year.isin([2014]) & (average.index.dayofweek > 4)]
    data_weekend_2015 = average[average.index.year.isin([2015]) & (average.index.dayofweek > 4)]
    data_weekend_2016 = average[average.index.year.isin([2016]) & (average.index.dayofweek > 4)]

    plt.figure(figsize=(15, 5))
    data_weekend_2014.plot()
    data_weekend_2015.plot()
    data_weekend_2016.plot()

    plt.ylabel('Temperatura', fontsize=12)
    plt.title('Average temperature on weekends in individual months in 2014-2016', fontsize=16)
    plt.show()

if __name__ == "__main__":
    main()



