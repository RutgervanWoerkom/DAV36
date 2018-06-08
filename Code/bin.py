import pandas as pd
def to_bin():
    data = pd.read_csv('../Data/clean/Changedtobits.csv', encoding = 'latin-1', low_memory = False)
    bins = [-1, 10, 20, 30, 40, 50,60,70,80,90,99.99,100]
    bins_2 = [-1,10,20,30,40,50,60,70,80,90,100]
    bins_3 = [-1,1,10,20,30,40,50,60,70,80,90,100]
    labels = [0,1,2,3,4,5,6,7,8,9,10]
    labels_2 = [0,1,2,3,4,5,6,7,8,9]
    data['%Leveringsrichting'.format()] = pd.cut(data['%Leveringsrichting'.format()], bins=bins, labels=labels)
    data['%Fysieke status'.format()] = pd.cut(data['%Fysieke status'.format()], bins=bins_2,labels=labels_2)
    data['%Slimme Meter'.format()] = pd.cut(data['%Slimme Meter'.format()], bins=bins_2,labels=labels_2)
    data['%SJV laag tarief'.format()] = pd.cut(data['%SJV laag tarief'.format()], bins=bins_3,labels=labels)
    data.drop(['Gemiddeld aantal telwielen', '%Defintieve aansl (NRM)'], axis = 1, inplace = True)
    data.to_csv('../Data/clean/finalclean3.0.csv',index = False)
    print(data.isnull().sum())


to_bin()


