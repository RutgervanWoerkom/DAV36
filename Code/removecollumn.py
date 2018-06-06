import pandas as pd
df = pd.read_csv('../Data/clean/combinedyears.csv')

df.drop('col3', axis = 1, inplace = True)