import matplotlib.pyplot as plt
import numpy as np

results1 = (21, 41, 22, 41, 42, 48, 20, 21, 20, 40, 40, 34, 21, 41, 47, 39, 43, 47, 28, 35, 49, 47, 22, 33, 30, 22, 29, 30, 41, 42)
group1 = (0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0)
sum_women1 = sum([results1[i] for i in range(len(group1)) if group1[i] == 0 ])
sum_men1 = sum([results1[i] for i in range(len(group1)) if group1[i] == 1 ])
avg_women1 = sum_women1/group1.count(0)
avg_men1 = sum_men1/group1.count(1)

results2 = (47, 49, 41, 31, 45, 24, 29, 22, 28, 24, 36, 28, 49, 40, 39, 39, 49, 26, 45, 26, 32, 30, 30, 41, 33)
group2 = (1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1)
sum_women2 = sum([results2[i] for i in range(len(group2)) if group2[i] == 0 ])
sum_men2 = sum([results2[i] for i in range(len(group2)) if group2[i] == 1 ])
avg_women2 = sum_women2/group2.count(0)
avg_men2 = sum_men2/group2.count(1)


results3 = (27, 44, 27, 40, 39, 42, 27, 28, 20, 30, 44, 38, 26, 37, 37, 27, 28, 30, 43, 37, 39, 26, 38, 47, 45, 40, 35)
group3 = (1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1)
sum_women3 = sum([results3[i] for i in range(len(group3)) if group3[i] == 0 ])
sum_men3 = sum([results3[i] for i in range(len(group3)) if group3[i] == 1 ])
avg_women3 = sum_women3/group3.count(0)
avg_men3 = sum_men3/group3.count(1)


data = [[avg_women1, avg_women2, avg_women3],
       [avg_men1, avg_men2, avg_men3]]
x = np.arange(3)
plt.figure(figsize=(12,7))
plt.bar(x + 0.00, data[0], width = 0.25, label='Women', color='#cc0000', edgecolor='k')
plt.bar(x + 0.25, data[1], width = 0.25, label='Men', color='#0066cc',edgecolor='k')
plt.xticks(x + 0.125, ['Group1','Group 2','Group 3'])
plt.yticks ( np.arange (0 , 39 , 3))
plt.title('The average number of points depending on gender')
plt.legend(loc ='lower left')
plt.show()

