from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
path='/home/iandersonpablo/Dev/DataScienceProjectTutorial/'

data = pd.read_csv("path/CsvFiles/stock.csv")
df = pd.DataFrame(data, columns=['ValueDate', 'Price'])

# Set the Date as Index
df['ValueDate'] = pd.to_datetime(df['ValueDate'])
df.index = df['ValueDate']
del df['ValueDate']


df.plot(figsize=(15, 6))
plt.show()
