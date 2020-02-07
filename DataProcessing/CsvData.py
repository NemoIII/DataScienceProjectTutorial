import pandas as pd

# data = pd.read_csv('./CsvFiles/acqua.csv')
data = pd.read_csv('../CsvFiles/input.csv')

# To read all in csv file
print(data)

# To read specific rows
print(data[:5]['salary'])

# To read specific columns
print(data.loc[:,['salary', 'name']])

# To read specific columns and rows
print(data.loc[[1, 3, 5], ['salary', 'name']])

# To read specific columns for a range of rows
print(data.loc[2:6, ['salary', 'name']])
