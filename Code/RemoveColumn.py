import pandas as pd
df = pd.read_csv('../Data/clean/combinedyears.csv', low_memory=False)

df.drop(['Gemiddeld aantal telwielen', 'MEETVERANTWOORDELIJKE', 'NETBEHEERDER', 'NETGEBIED', 'LANDCODE', 'WOONPLAATS', 'VERBRUIKSSEGMENT', '%Defintieve aansl (NRM)'], axis = 1, inplace = True)

df.to_csv('../Data/clean/CombinedRemoved.csv',index = False)