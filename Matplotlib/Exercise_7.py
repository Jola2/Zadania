import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

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
dictionary = Counter(arr)
print(dictionary)


fig1, axis = plt.subplots(figsize=(12,8))
axis.pie([28,19,3], explode=(0, 0, 0.2,), labels=('zielony','niebieski','czerwony'), colors = ('g','b','r'),
         autopct= ("%2d"% (3)), radius=0.8,shadow=True, startangle=90)

plt.axis('equal')
plt.show()
