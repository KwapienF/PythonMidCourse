ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

portslist = [(a,b) for a in ports for b in ports if a != b]
print(portslist)


portslist = [(a,b) for a in ports for b in ports if a < b]
print(portslist)