import csv

clean = open('../Data/clean/cleandata2015.csv','w')

with open("../Data/data2015.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if 'STRAATNAAM' in row:
            clean.write(','.join(row))
            clean.write(',JAARTAL')
        elif 'AMSTERDAM' in row or 'AMSTERDAM ZUIDOOST' in row:
            clean.write(','.join(row))
            clean.write(',2015')
        clean.write('\n')

