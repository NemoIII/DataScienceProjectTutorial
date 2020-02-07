import pandas as pd

data = pd.read_excel('./XlsxFiles/input.xls')
data2 = pd.read_excel('./XlsxFiles/input2.xls')

# Reading an Excel File
print(data)

# Reading Specific Columns and Rows
print (data.loc[[1,3,5],['salary','name']])

# Reading Multiple Excel Sheets
print("****Result Sheet 1****")
print (data[0:5]['salary'])
print("")
print("***Result Sheet 2****")
print (data2[0:5]['zipcode'])
