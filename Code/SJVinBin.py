import pandas as pd
import statistics

data = pd.read_csv('../Data/clean/finalclean3.0.csv', encoding = 'latin-1', low_memory = False)

elk = []

for index in range(len(data)):
    if data.loc[index, 'PRODUCTSOORT'] == 0:
        elk.append(data.loc[index, 'SJV'])

print(statistics.mean(elk))



#def to_bin():
#    bins_SJV = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 100000]
#    labels_SJV = [0,1,2,3,4,5,6,7,8,9,10]
#   elk['SJV'.format()] = pd.cut(data['SJV'.format()], bins=bins_SJV, labels=labels_SJV)
#    elk.to_csv('../Data/clean/SJV_in_bin.csv',index = False)
#    print(elk.isnull().sum())

#to_bin()


