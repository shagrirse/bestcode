import pandas as pd

df = pd.read_csv(r'sportsday\PFP Sports Day Registration.csv')
individual = df[df['Type of registration'] == 'Individual'].dropna(axis=1)
ultimate = df[df['Sport'] == 'Ultimate Frisbee'].dropna(axis=1)
bball = df[df['Sport'] == '3v3 Basketball'].dropna(axis=1)
cbal = df[df['Sport'] == "Captain's Ball"].dropna(axis=1)
ssc = df[df['Sport'] == "Street Soccer"].dropna(axis=1)
# To CSV
individual.to_csv(r"sportsday\output\Individual List.csv", index=False)
ultimate.to_csv(r"sportsday\output\Ultimate Teams.csv", index=False)
bball.to_csv(r'sportsday\output\Basketball Teams.csv', index=False)
cbal.to_csv(r"sportsday\output\Captain's Ball.csv", index=False)
ssc.to_csv(r"sportsday\output\Street Soccer.csv", index=False)

print(individual)