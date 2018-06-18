import pandas as pd
import statistics
import numpy

data = pd.read_csv('../Data/clean/finalclean3.0.csv', encoding = 'latin-1', low_memory = False)

elk = []

for index in range(len(data)):
    if data.loc[index, 'PRODUCTSOORT'] == 0:
        elk.append(data.loc[index, 'SJV'])

print(statistics.mean(elk))

grouped = data.groupby('PRODUCTSOORT')
group0 = grouped.get_group(0)
group1 = grouped.get_group(1)

def to_bin():
    bins_SJV_0 = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 100000]
    labels_SJV_0 = [0,1,2,3,4,5,6,7,8,9,10]
    data['SJV'.format()] = pd.cut(group0['SJV'.format()], bins=bins_SJV_0, labels=labels_SJV_0)
    

to_bin()

CovA = []
CovB = []

for i in range(len(data)):
    if data.loc[i,'PRODUCTSOORT'] == 0:
        CovA.append(data.loc[i,'SJV'])
        CovB.append(data.loc[i,'%Leveringsrichting'])

print(numpy.cov(CovA,CovB)[0][1])