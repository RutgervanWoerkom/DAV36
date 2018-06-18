import pandas as pd
import numpy as np


data = pd.read_csv('../Data/clean/finalclean3.0.csv')

data[:5]

data['PRODUCTSOORT'].value_counts()[:5]


