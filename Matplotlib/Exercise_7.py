import numpy as np
import matplotlib.pyplot as plt

arr = ['zielony', 'zielony', 'zielony', 'zielony', 'zielony', 'zielony',
       'niebieski', 'niebieski', 'zielony', 'zielony', 'zielony',
       'zielony', 'zielony', 'niebieski', 'zielony', 'zielony',
       'niebieski', 'zielony', 'zielony', 'zielony', 'niebieski',
       'niebieski', 'czerwony', 'zielony', 'czerwony', 'niebieski',
       'niebieski', 'niebieski', 'zielony', 'zielony', 'niebieski',
       'niebieski', 'niebieski', 'niebieski', 'zielony', 'niebieski',
       'niebieski', 'zielony', 'niebieski', 'zielony', 'zielony',
       'czerwony', 'zielony', 'niebieski', 'zielony', 'zielony',
       'niebieski', 'niebieski', 'zielony', 'zielony']

# calculate the frequency of each color
data = [arr.count('zielony'), arr.count('niebieski'), arr.count('czerwony')]
sizes = np.array([data])
labels = ['zielony', 'niebieski', 'czerwony']

# a function that returns the actual values in a matplotlib pie chart
def absolute_value(val):
    return np.round(val/100.*sizes.sum(), 0)

def main():
    # create a pie chart showing the popularity of the results
    fig1, axis = plt.subplots(figsize=(12, 8))
    axis.pie(data, labels=labels, explode=(0, 0, 0.2,), colors=('g', 'b', 'r'),
             autopct=absolute_value, radius=0.8, shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()