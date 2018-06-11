import pandas as pd
df = pd.read_csv('../Data/clean/CombinedRemoved.csv')

df.loc[df.PRODUCTSOORT == 'ELK', 'PRODUCTSOORT'] = 0
df.loc[df.PRODUCTSOORT == 'GAS', 'PRODUCTSOORT'] = 1


df.to_csv('../Data/clean/Changedtobits.csv', index=False)