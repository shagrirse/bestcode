import pandas as pd
import numpy
import openpyxl
import re

df = pd.read_csv(r'sportsday\PFP Sports Day Registration.csv')
#individuals
individual = df[df['Type of registration'] == 'Individual'].dropna(axis=1)
ind_ssc = individual[individual['Desired sport'] == "Street Soccer"]
ind_bball = individual[individual['Desired sport'] == "3 v 3 Basketball"]
ind_cbal = individual[individual['Desired sport'] == "Captain's Ball"]
#teams
bball = df[df['Sport'] == "3 v 3 Basketball"].dropna(axis=1)
cbal = df[df['Sport'] == "Captain's Ball"].dropna(axis=1)
ssc = df[df['Sport'] == "Street Soccer"].dropna(axis=1)
# To CSV
with pd.ExcelWriter(r'sportsday\output\Compiled.xlsx') as pp:
    individual.to_excel(pp, index=False, sheet_name='Individuals')
    ind_ssc.to_excel(pp, index=False, sheet_name='Individual Street Soccer')
    ind_bball.to_excel(pp, index=False, sheet_name='Individual Basketball')
    ind_cbal.to_excel(pp, index=False, sheet_name="Individual Captain's Ball")

    bball.to_excel(pp, index=False, sheet_name='Basketball Team')
    cbal.to_excel(pp, index=False, sheet_name='Captains Ball Team')
    ssc.to_excel(pp, index=False, sheet_name='Street Soccer Team')
# Admin Numbers
col = [col for col in df.columns if "Admin" in col]
admin_no = df[col]
df['Number'] = df[col].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1).str.replace(',', '\n')
admin_no = df['Number'].str.replace("P", "")

admin_no.to_csv(r'sportsday\admin number.csv', index=False)
# #Execute Later
# admin_no = pd.read_csv(r'sportsday\admin number.csv')
# admin_no = admin_no.iloc[:,0].str.replace("P", "")
# print(type(admin_no))
# admin_no.to_csv(r'sportsday\admin number.csv', index=False)