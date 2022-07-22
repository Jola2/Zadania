import matplotlib.pyplot as plt
import pandas as pd


def main():
    # read the Excel file
    df = pd.read_excel('c:/Users/admin/Desktop/Dane_do_zadan/mieszkania_krakow_krowodrza.xlsx', sheet_name='krowodrza')
    print(df)

    # draw a graph between the size of the flat and the price
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.scatter(x="area", y="price", data=df, facecolor='red', edgecolor='k', marker='^')
    plt.xlabel('Flat area', fontsize='14', horizontalalignment='center')
    plt.ylabel('Price', fontsize='14', horizontalalignment='center')
    plt.title('Area of flats and their prices', fontsize='16')
    plt.show()

    # create a graph where the color of the triangles will depend on type of building
    df1 = df[df['type'] == 'kamienica']
    df2 = df[df['type'] == 'blok']
    df3 = df[df['type'] == 'apartamentowiec']
    df4 = df[df['type'] == 'brak informacji']
    plt.scatter(df1['area'], df1['price'], color='yellow', marker='^', edgecolor='k', label='kamienica')
    plt.scatter(df2['area'], df2['price'], color='red', marker='^', edgecolor='k', label='blok')
    plt.scatter(df3['area'], df3['price'], color='green', marker='^', edgecolor='k', label='apartamentowiec')
    plt.scatter(df4['area'], df4['price'], color='blue', marker='^', edgecolor='k', label='brak informacji')
    plt.xlabel('Flat area', fontsize='14', horizontalalignment='center')
    plt.ylabel('Price', fontsize='14', horizontalalignment='center')
    plt.title('Building types', fontsize='16')
    plt.legend()
    plt.show()

    # create a bar chart showing the average flat price from taking into account the division into the floor.
    plt.figure(figsize=(18, 6))
    data = df.groupby('floor')['price'].mean()
    data.plot(kind='bar', title="Average prices of flats taking into account the division into floors ", rot=0)
    plt.show()

    # filter out those observations where the year was not given
    new_df = df[df.year != 'brak informacji'].copy()
    arr = new_df['year']

    # create a new column "Century_and_decade" and assign to it information from what decade
    # and century the building is.
    decades = []
    centuries = []
    for year in arr:
        decade = str(year)
        decade = decade[-2]
        decade = 'lata ' + decade + '0'
        decades.append(decade)
        if int(year) % 100 == 0:
            century = int(year) // 100
        else:
            century = int(year) // 100 + 1
        century = str(century) + ' wiek'
        centuries.append(century)

    new_df['Century'] = centuries
    new_df['Decade'] = decades
    new_df['Century_and_decade'] = new_df['Century'] + ' ' + new_df['Decade']
    print(new_df)

    summary = new_df.groupby(pd.Grouper(key='Century_and_decade')).describe().T
    print(summary)

    # create charts that compare prices according to the decade from which comes the building
    # one graph corresponds to one statistic summarizing (information from summary)
    df = summary.loc[('price', 'min')]
    df.plot(kind='bar', figsize=(20, 5), title='The minimum price of flat depends on the decade', rot=45)
    plt.show()

    df = summary.loc[('price', 'max')]
    df.plot(kind='bar', figsize=(18, 4), title='The maximum price of flat depends on the decade', rot=45)
    plt.show()

    df = summary.loc[('price', 'mean')].sort_index()
    df.plot(kind='bar', figsize=(20, 5), title='The average price of flat depends on the decade', rot=45)
    plt.show()

    df = summary.loc[('price', 'std')]
    df.plot(kind='bar', figsize=(20, 5), title='The standard deviation of flat prices depending on the decade', rot=45)
    plt.show()

    df = summary.loc[('price', '25%')]
    df.plot(kind='bar', figsize=(20, 5), title='First quartile (Q1) results depending on the decade', rot=45)
    plt.show()

    df = summary.loc[('price', '50%')]
    df.plot(kind='bar', figsize=(20, 5), title='Second quartile (Q2) depending on the decade', rot=45)
    plt.show()

    df = summary.loc[('price', '75%')]
    df.plot(kind='bar', figsize=(20, 5), title='Third quartile (Q3) depending on the decade', rot=45)
    plt.show()


if __name__ == '__main__':
    main()
