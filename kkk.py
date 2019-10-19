import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('AB_NYC_2019.csv')
df = pd.DataFrame(data)
df['last_review'] = pd.to_datetime(df['last_review'])
brooklyn = df[ df['neighbourhood_group'] == 'Brooklyn' ].dropna().set_index('last_review')
brooklyn.sort_index(inplace=True)
brooklyn['reviews_per_month'].rolling(20).mean().plot()
plt.show()