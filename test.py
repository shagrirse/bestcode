import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('AB_NYC_2019.csv')
df = pd.DataFrame(data)
new_df = df.dropna()

checknull = new_df.isnull().sum()

plt.boxplot(new_df['reviews_per_month'])
plt.show()