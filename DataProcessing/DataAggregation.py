import pandas as pd
import numpy as np

'''Applying Aggregations on DataFrame'''
df = pd.DataFrame(np.random.randn(10, 4), index = pd.date_range('1/1/2000', periods=10), columns=['A', 'B', 'C', 'D'])
print(df)

r = df.rolling(window=3, min_periods=1, center=True)
print(r)
print('--'* 24)

'''Apply Aggregation on a Whole Dataframe'''
df = pd.DataFrame(np.random.randn(10, 4), index= pd.date_range('1/1/2000', periods=10), columns=['A', 'B', 'C', 'D'])
print(df)
print('--'* 24)

r = df.rolling(window=3, min_periods=1)
print(r.aggregate(np.sum))
print('--'* 24)

'''Apply Aggregation on a Single Column of a Dataframe'''
df = pd.DataFrame(np.random.randn(10, 4), index= pd.date_range('1/1/2000', periods=10), columns= ['A', 'B', 'C', 'D'])
print(df)

r = df.rolling(window=3, min_periods=1)
print(r['A'].aggregate(np.sum))
print('--'* 24)

'''Apply Aggregation on Multiple Columns of a DataFrame'''
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print(df)
r = df.rolling(window=3,min_periods=1)
print(r[['A','B']].aggregate(np.sum))
print('--'* 24)
