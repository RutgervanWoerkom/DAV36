import pandas as pd
def to_bin():
    data = pd.read_csv('../Data/clean/Changedtobits.csv', encoding = 'latin-1', low_memory = False)
    bins = [0, 10, 20, 30, 40, 50,60,70,80,90,99.99,100]
    bins_2 = [0,10,20,30,40,50,60,70,80,90,100]
    bins_3 = [0,1,10,20,30,40,50,60,70,80,90,100]
    labels = [0,1,2,3,4,5,6,7,8,9,10]
    labels_2 = [0,1,2,3,4,5,6,7,8,9]
    data['%Leveringsrichting'.format()] = pd.cut(data['%Leveringsrichting'.format()], bins=bins, labels=labels)
    data['%Fysieke status'.format()] = pd.cut(data['%Fysieke status'.format()], bins=bins_2,labels=labels_2)
    data['%Slimme Meter'.format()] = pd.cut(data['%Slimme Meter'.format()], bins=bins_2,labels=labels_2)
    data['%SJV laag tarief'.format()] = pd.cut(data['%SJV laag tarief'.format()], bins=bins_3,labels=labels)
    data.to_csv('../Data/clean/bins.csv',index = False)

to_bin()