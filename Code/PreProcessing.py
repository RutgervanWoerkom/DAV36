import csv

clean = open('../Data/cleandata2018.csv','w')

with open("../Data/2018unicode.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        clean.write(','.join(row))
        if 'STRAATNAAM' in row:
            clean.write(',JAARTAL')
        elif 'AMSTERDAM' in row or 'AMSTERDAM ZUIDOOST' in row:
            clean.write(',2018')
        clean.write('\n')