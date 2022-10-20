ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

portslist = [(a,b) for a in ports for b in ports if a != b]
print(portslist)


portslist = [(a,b) for a in ports for b in ports if a < b]
print(portslist)

# przerobienie powyzszch list na generator

gen1 = ((a,b) for a in ports for b in ports if a != b)


gen2 = ((a,b) for a in ports for b in ports if a < b)

for x in gen1:
    print(x)
print('-'*50)
while True:
    try:
        print(next(gen2))
    except StopIteration:
        print("Koniec generatora")
        break
gen1 = ((a,b) for a in ports for b in ports if a != b)
len1 = 0
for x in gen1:
    len1 += 1
    print(x)
print('Dlugosc gen1 wynosi: ', len1)
print('-'*50)

gen2 = ((a,b) for a in ports for b in ports if a < b)
len2 = 0
while True:
    try:
        print(next(gen2))
        len2 += 1
    except StopIteration:
        print("Koniec generatora")
        print('Dlugosc gen2 wynosi: ', len2)
        break