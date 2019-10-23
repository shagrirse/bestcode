import pandas as pd

df = pd.read_csv('PFP Sports Day Registration.csv')
ultimate = df[df['Sport'] == 'Ultimate Frisbee'].dropna(axis=1)
ultimate.to_csv('Ultimate Teams.csv', index=False)
bball = df[df['Sport'] == '3v3 Basketball'].dropna(axis=1)
bball.to_csv('Basketball Teams.csv', index=False)
cbal = df[df['Sport'] == "Captain's Ball"].dropna(axis=1)
cbal.to_csv("Captain's Ball.csv", index=False)
ssc = df[df['Sport'] == "Street Soccer"].dropna(axis=1)
ssc.to_csv("Street Soccer.csv", index=False)