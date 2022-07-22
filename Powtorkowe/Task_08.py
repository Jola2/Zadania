import matplotlib.pyplot as plt
import pandas as pd


def main():
    # read the csv file
    df = pd.read_csv('c:/Users/admin/Desktop/Dane_do_zadan/wig20_m.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    # plot the changes of the Volume variable over the years
    x = df['Date']
    y = df['Volume']
    plt.figure(figsize=(17, 6))
    plt.plot(x, y)
    plt.title('Change of the variable Volume  over the years')
    plt.show()

    # show the value of open, close, high and low in one chart
    df.drop("Volume", axis=1).set_index("Date").plot(figsize=(20, 8))
    plt.title('Change of variables over the years')
    plt.legend()
    plt.show()

    # show the same data in 4 separate charts, but let it form as one whole
    fig = plt.figure(figsize=(20, 12))
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
    plt.plot(x, df['Open'], label='Open', color='k', linestyle='dotted')
    ax1.set_title('Change of the variable Open', fontdict={'fontsize': 12})
    rect = ax1.patch
    rect.set_facecolor('#D2B48C')

    ax2 = plt.subplot2grid((3, 3), (0, 2), rowspan=2)
    plt.plot(x, df['High'], label='High', color='k', linestyle='dashdot')
    ax2.set_title('Change of the variable High', fontdict={'fontsize': 12})
    rect = ax2.patch
    rect.set_facecolor('#DEB887')

    ax3 = plt.subplot2grid((3, 3), (1, 0))
    plt.plot(x, df['Low'], label='Low', color='k', linestyle='dashed')
    ax3.set_title('Change of the variable Low', fontdict={'fontsize': 12})
    rect = ax3.patch
    rect.set_facecolor('#FFDEAD')

    ax4 = plt.subplot2grid((3, 3), (1, 1))
    plt.plot(x, df['Close'], label='Close', color='k', linestyle='solid')
    ax4.set_title('Change of the variable Close', fontdict={'fontsize': 12})
    rect = ax4.patch
    rect.set_facecolor('#FFF8DC')

    fig.tight_layout()
    plt.show()

    # show on one bar chart the minimum, average and maximum of CLose
    data_close = df.resample('Y', on='Date').agg(minimum=('Close', 'min'),
                                                 maximum=('Close', 'max'),
                                                 average=('Close', 'mean'))
    data_2015_2020 = data_close[data_close.index.year.isin(range(2015, 2021))]
    data_2015_2020.plot(figsize=(20, 5), title='Minimum, maximum and average of the variable Close in 2015-2020',
                        kind='bar')
    plt.show()


if __name__ == '__main__':
    main()
