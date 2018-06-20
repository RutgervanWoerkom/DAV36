import pandas as pd
import statistics
import numpy

data = pd.read_csv('../Data/clean/finalclean3.0.csv', encoding = 'latin-1', low_memory = False)

elk = []
gas = []

for index in range(len(data)):
    if data.loc[index, 'PRODUCTSOORT'] == 0:
        elk.append(data.loc[index, 'SJV'])
    elif data.loc[index, 'PRODUCTSOORT'] == 1:
        gas.append(data.loc[index, 'SJV'])

print(statistics.mean(elk))
print(statistics.mean(gas))

grouped = data.groupby('PRODUCTSOORT')
group0 = grouped.get_group(0)
group1 = grouped.get_group(1)

def to_bin():
    bins_SJV_0 = [0, 1500, 1700, 1900, 2100, 2300, 2600, 3000, 3500, 4300, 6500, 100000]
    labels_SJV_0 = [0,1,2,3,4,5,6,7,8,9,10]
    data['SJV'.format()] = pd.cut(group0['SJV'.format()], bins=bins_SJV_0, labels=labels_SJV_0)
    
to_bin()

CovA = []
CovB = []

for i in range(len(data)):
    if data.loc[i,'PRODUCTSOORT'] == 0:
        CovA.append(data.loc[i,'SJV'])
        CovB.append(data.loc[i,'%Leveringsrichting'])

print(data.groupby('SJV').count())

print(numpy.cov(CovA,CovB)[0][1])