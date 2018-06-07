import pandas as pd
df = pd.read_csv('../Data/clean/combinedyears.csv')

df.drop(['NETBEHEERDER', 'NETGEBIED', 'LANDCODE', 'WOONPLAATS', 'VERBRUIKSSEGMENT'], axis = 1, inplace = True)

print(df)

df.to_csv('../Data/clean/CombinedRemoved.csv',index = False)