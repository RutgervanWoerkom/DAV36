import csv

clean = open('../Data/cleandata2018.csv','w')

with open("../Data/2018unicode.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if 'AMSTERDAM' in row or 'AMSTERDAM ZUIDOOST' in row or 'STRAATNAAM' in row:
            clean.write(','.join(row))
            clean.write('\n')