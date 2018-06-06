import csv

clean = open('../Data/clean/combinedyears.csv','w')

with open('../Data/clean/cleandata2018.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if 'STRAATNAAM' in row:
            clean.write(','.join(row))
            clean.write('\n')
        elif 'AMSTERDAM' in row or 'AMSTERDAM ZUIDOOST' in row:
            clean.write(','.join(row))
            clean.write('\n')

with open('../Data/clean/cleandata2017.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if 'AMSTERDAM' in row or 'AMSTERDAM ZUIDOOST' in row:
            clean.write(','.join(row))
            clean.write('\n')
    
with open('../Data/clean/cleandata2016.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if 'AMSTERDAM' in row or 'AMSTERDAM ZUIDOOST' in row:
            clean.write(','.join(row))
            clean.write('\n')

with open('../Data/clean/cleandata2015.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if 'AMSTERDAM' in row or 'AMSTERDAM ZUIDOOST' in row:
            clean.write(','.join(row))
            clean.write('\n')
        
with open('../Data/clean/cleandata2014.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if 'AMSTERDAM' in row or 'AMSTERDAM ZUIDOOST' in row:
            clean.write(','.join(row))
            clean.write('\n')

