
raw = open("../Data/2018Data.csv",encoding='utf-8').read()

cleaned = open('../Data/cleandata2018.csv')

for i in cleaned:
    print(i)

cleaned.write("hello world")
