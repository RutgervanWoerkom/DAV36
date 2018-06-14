import pandas as pd
df = pd.read_csv('../Data/clean/CombinedRemoved.csv')

df.loc[df.PRODUCTSOORT == '0', 'PRODUCTSOORT'] = 0
df.loc[df.PRODUCTSOORT == '1', 'PRODUCTSOORT'] = 1

cell=[]
for cell in range:
    cell = df.loc[df.PRODUCTSOORT == '0', 'PRODUCTSOORT']

df.to_csv('../Data/clean/Changedtobits.csv', index=False)