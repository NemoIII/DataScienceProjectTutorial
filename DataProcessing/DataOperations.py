import numpy as np
import pandas as pd

# more than one dimensions
a = np.array([[1, 2], [3, 4]])
print(a)

# # minimun dimensios
b = np.array([1, 2, 3, 4, 5], ndmin=2)
print(b)

# #dtype parameter
c = np.array([1, 2, 3], dtype=complex)
print(c)

# # using pandas
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)

# #creating as indexed DataFrame using arrays
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)

