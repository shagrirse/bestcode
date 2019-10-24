import pandas as pd
import openpyxl

df = pd.read_csv(r'sportsday\PFP Sports Day Registration.csv')
#individuals
individual = df[df['Type of registration'] == 'Individual'].dropna(axis=1)
ind_ssc = individual[individual['Desired sport'] == "Street Soccer"]
ind_bball = individual[individual['Desired sport'] == "3 v 3 Basketball"]
ind_cbal = individual[individual['Desired sport'] == "Captain's Ball"]
ind_fris = individual[individual['Desired sport'] == "Ultimate Frisbee"]
#teams
ultimate = df[df['Sport'] == 'Ultimate Frisbee'].dropna(axis=1)
bball = df[df['Sport'] == '3v3 Basketball'].dropna(axis=1)
cbal = df[df['Sport'] == "Captain's Ball"].dropna(axis=1)
ssc = df[df['Sport'] == "Street Soccer"].dropna(axis=1)
# To CSV
with pd.ExcelWriter(r'sportsday\output\Compiled.xlsx') as pp:
    individual.to_excel(pp, index=False, sheet_name='Individuals')
    ultimate.to_excel(pp, index=False, sheet_name='Ultimate Frisbee Team')
    bball.to_excel(pp, index=False, sheet_name='Basketball Team')
    cbal.to_excel(pp, index=False, sheet_name='Captains Ball Team')
    ssc.to_excel(pp, index=False, sheet_name='Street Soccer Team')
