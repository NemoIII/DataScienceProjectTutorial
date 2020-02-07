from sqlalchemy import create_engine
import pandas as pd
from pandas.io import sql

data = pd.read_csv('../CsvFiles/input.csv')
# Create th db engine
engine = create_engine('sqlite:///:memory:')

# store the dataframe as a table
data.to_sql('data_table', engine)
'''
# Query 1 on the relational table
result1 = pd.read_sql_query('SELECT * FROM data_table', engine)
print("Result 1")
print(result1)
print(' ')

# Query 2 on the relational table
result2 = pd.read_sql_query('SELECT dept, sum(salary) FROM data_table group by dept', engine)
print("Result 2")
print(result2)
print(' ')
'''

'''Inserting Data to Relational Tables'''
'''# Store the Data in a relational table
data.to_sql('data_table', engine)

# Insert another row
sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)', engine, params=[('id',9,'Ruby',711.20,'2015-03-27','IT')])

# Read from the relational table
res = pd.read_sql_query('SELECT ID,Dept,Name,Salary,start_date FROM data_table', engine)
print(res)'''

'''Deleting Data from Relational Tables'''
# Deleting
sql.execute('Delete from data_table where name = (?) ', engine, params=[('Gary')])

result = pd.read_sql_query('SELECT ID, Dept, Name, Salary, start_date FROM data_table', engine)
print(result)
