import datetime
netto = 100
brutto = 120
# netto <= brutto always

assert netto <= brutto, 'netto <= brutto always' # assert założenie zakłada ze tak ma byc z danymi jak to sie nie zgodzi to bedzie assertionerror po przecinku treść

orderDate = datetime.date(2022,11,13)
deliveryDate = datetime.date(2022,10,18)
# order date <= delivery ALWAYS
assert orderDate <= deliveryDate, 'order date <= delivery ALWAYS'

# asser opoznia dzialanie programu
# CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!! CMD !!!
# W CMD command line  uruchamiamy python, assert False. Wywali blad. Dajemy SET PYTHONOPTIMIZE=TRUE. robimy exit() i uruchamiamy python znow i dajmey polecenie
# któe spowoduje blad czyli assert False i stanie sie to ze nie wywali blad wylaczylismy wlasnie sprawdzanie assertow aby przyspieszyc program
# jesli chcemy wrocic do srodowiksa gdzie assert dzialaja to robimy exit i ustawiamy zmienna srodowiskowa na pythonoptimize =   po rowna sie nic tylko enter


