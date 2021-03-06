import csv

clean = open('../Data/clean/cleandata2018.csv','w')

with open("../Data/fix2018.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if 'STRAATNAAM' in row:
            clean.write('JAARTAL,')
            clean.write(','.join(row))            
        elif 'AMSTERDAM' in row or 'AMSTERDAM ZUIDOOST' in row:
            clean.write('"2018",')
            clean.write(','.join(row))
        clean.write('\n')