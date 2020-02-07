import pandas as pd

data = pd.read_json('../JsonFiles/input.json')
# To read a json file
print(data)

# To read specific columns and rows
print(data.loc[[1, 3, 5], ['Salary', 'Name']])

# To read Json file as records
print(data.to_json(orient='records', lines=True))
