import numpy as np

arr = np.array([[61,59,88,74,26,28],[52,4,67,82,28,44],[79,81,78,100,73,53],[15,67,64,76,43,42]])
print(arr)

# calculate the sum, maximum, minimum, median, average over, cumulative sum,
# product of values, cumulative product of values by 3 ways

# 1 way: calculate along the whole
print('Along the whole')
print('Sum:',np.sum(arr))
print('Minimum:',np.min(arr))
print('Maximum:',np.max(arr))
print('Median:',np.mean(arr))
print('Average over:',np.std(arr))
print('Cumulative sum:',np.cumsum(arr))
print('Product of values:',np.prod(arr))
print('Cumulative product of values:',np.cumprod(arr), end='\n'+'-'*20+'\n')

# 2 way: calculate along the columns
print('Along the columns')
print('Sum:',np.sum(arr,axis=1))
print('Minimum:',np.min(arr,axis=1))
print('Maximum:',np.max(arr,axis=1))
print('Median:',np.mean(arr,axis=1))
print('Average over:',np.std(arr,axis=1))
print('Cumulative sum:',np.cumsum(arr,axis=1))
print('Product of values:',np.prod(arr,axis=1))
print('Cumulative product of values:',np.cumprod(arr,axis=1), end='\n'+'-'*20+'\n')

# 3 way:calculate along the rows
print('Along the rows')
print('Sum:',np.sum(arr,axis=0))
print('Minimum:',np.min(arr,axis=0))
print('Maximum:',np.max(arr,axis=0))
print('Median:',np.mean(arr,axis=0))
print('Average over:',np.std(arr,axis=0))
print('Cumulative sum:',np.cumsum(arr,axis=0))
print('Product of values:',np.prod(arr,axis=0))
print('Cumulative product of values:',np.cumprod(arr,axis=0))



