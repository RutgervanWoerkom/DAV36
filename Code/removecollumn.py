import pandas as pd
df = pd.read_csv('../Data/clean/combinedyears.csv')
writer = open('../Data/clean/collumnsremoved.csv','w')

df.drop(['MEETVERANTWOORDELIJKE', 'NETBEHEERDER', 'NETGEBIED', 'LANDCODE', 'WOONPLAATS', 'VERBRUIKSSEGMENT'], axis = 1, inplace = True)


print(df)
