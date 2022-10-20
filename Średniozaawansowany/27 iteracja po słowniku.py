workDays = [19,21,22,21,20,22]
months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthsDays = dict(zip(months,workDays)) # zamiana na slownik {}  a nie na liste po prez list
# klucz to miesiac wartosc to ilosc dni roboczych
print(monthsDays)

for key in monthsDays:
    print('key is ',key,'value is ', monthsDays[key])
# to samo inaczej
for value in monthsDays.values(): # zwrocu wsystkie wartosci ze slownika
    print('The value is: ', value)

for value, key in zip(monthsDays.values(),monthsDays.keys()): # zwrocu wsystkie wartosci ze slownika
    print('The value is: ', value, 'for key: ',key)

# LAB WPLATOMAT
banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
banknotes_coins2 = []
for i in banknotes_coins:
    banknotes_coins2.append(0)
dict_denominations = dict(zip(banknotes_coins, banknotes_coins2))
print(dict_denominations)
dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1
for k,v in zip(dict_denominations.keys(),dict_denominations.values()):
    print('Bankomat posiada ilość ','%6.2f'%(v),' nominału ',k, ' co daje nam razem ','%6.2f'%(v*k), 'zł') # mozna tez f'{v:.2f}' !!!!!!!!
#    '%6.2f' % (v) 6 ile miejsca na liczbe przeznaczamy ___.__ 123.56 kropka jest czwarta po kropce 2 to ile po przecinku ma byc miescj a f floating liczba a w anwaisie za procent podstawiamy to co chcemy