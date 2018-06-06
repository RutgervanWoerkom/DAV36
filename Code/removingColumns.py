import pandas as pd
import numpy as np

df = pd.read_csv('../Data/clean/combinedyears.csv', error_bad_lines=False)

#print(df)

#df.drop(['B', 'C'], axis=1)