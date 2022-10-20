workDays = [19,21,22,21,20,22]
print(workDays)

print(workDays[2])
# co jesli chce ponumerowac elementy w liscie  i wiedziec jakie numery zostaly przyznane
enumerateDays = list(enumerate(workDays))
print(enumerateDays)
# w for mozna tez wybrac dwa elementy ktore maja rpzez petle przechodzic

for position, value in enumerateDays:
    print('pozycja: ',position,'=', 'wartość: ',value)

# zip - laczy dwie niezalezne listy po przez dodanie do siebie elementow na danych pozycjach
months = ['I', 'II', 'III', 'IV', 'V', 'VI']
monthsworkDays = list(zip(months,workDays))
print(monthsworkDays)

for m,d in monthsworkDays:
    print('Miesiąc ', m, 'ma ', d, ' dni pracujących')

# lista enumerowana powstala z list zipowanym xD WTF?! Da się:

for pos, (m,d) in enumerate(zip(months,workDays)): # pos odczyta sobie z enumerate a (m,d) odczyta sobie z argumentu enumerate czyli z polaczycnhc list
    print(pos,m,d) # enumerate nie konwertujemy na liste bo z enumerate chcemy tylko liczby pozycje a md bierze ju z z zip ktora jest lista samam w sobie wiec luss
    

