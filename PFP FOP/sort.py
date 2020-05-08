import pandas as pd
from sklearn.utils import shuffle
import matplotlib

data = pd.read_csv('PFP FOP\GLs.csv')
names = data['Full Name'].str.upper()

df = pd.DataFrame(names)
df.to_csv('PFP FOP\As.csv', index=False)
df.py