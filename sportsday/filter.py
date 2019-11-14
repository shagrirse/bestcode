import pandas as pd
import re

data1 = pd.read_csv(r'sportsday\Numbers.csv')
name = data1['Name'].str.title()
number = data1['Admin Number'].str.replace('P', '')
data = pd.concat([name, number], axis=1, sort=False)
print(data)
data.to_csv(r'sportsday\Numbers1.csv', index=False)