import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('salaries_1985to2018.csv')
df = pd.DataFrame(data, columns=['player_id', 'league'])

with open('aa.csv', 'w', newline="") as a:
    df.to_csv(a, index=False)

plt.hist(df, bins=10)