import pandas as pd
import random

data = pd.read_csv('JP10 Class List.csv')
p = data['CLASS'].tolist()
random.shuffle(p)
print(p)
a = pd.DataFrame(p)
print(a)