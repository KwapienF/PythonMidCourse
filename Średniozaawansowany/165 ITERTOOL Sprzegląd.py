import itertools
import operator

data = [1,2,3,4,5]
result = itertools.accumulate(data,operator.mul) # accumulate przyjmyje obeikt iterable a drgui arg to funkcja jaka ma wykoanc na tym argumencieoperator mul to mnoznie czyli pomnzy eleemtny listy przez siebie
for each in result:
    print(each)
print('-'*100)
data = [1,2,13,4,5]
result = itertools.accumulate(data,max) # max wyswietla najwieksza wartosc do tej pory znalezioną
for each in result:
    print(each)
print('-'*100)
for i in itertools.count(10,3): # policzy od 10  co 3 przeskok liczby zakonczy na 22 bo ostatnia liczba to19  a jest mniejsza od 20
    print(i)
    if i> 20:
        break
print('-'*100)
months = ['Jan','Feb','Mar']
# for m in itertools.cycle(months): # wczytuje w kołko z listy miesiace
#     print(m)

print('-' * 100)

color_basic = ['red','yellow']
color_mix = ['green','orange']
result = itertools.chain(color_basic,color_mix)
for m in result:
    print(m)
print('-'*100)
cars = ['Ford','Opel','Toyota','Skoda']
selections = [True,False,True,False]
result = itertools.compress(cars,selections) # compress zwroci tylko te elementy ktore maja wartosc True na tych samych pozycjach w drugiej liscie
for m in result:
    print(m)
print('-'*100)
data = [1,2,3,4,5,6,7,8,9,10,1]
result = itertools.dropwhile(lambda x: x<5, data) # drophile opusci wartosci dopoki nie spelni sie ten warunek dlatego opuscilo 1 2 3 4
# monza tez uzywc takewhile czyli bedzie na odwrot poberze  te wartosci az do czasu kiedy zacznie sie spelniac warunek
for each in result:
    print(each)
print('-'*100)
data = [1,2,3,4,5,6,7,8,9,10,1]
result = itertools.filterfalse(lambda x: x<5, data) # filterfalse opsuzcza wszystkie wartosci ktore nie spelniaja warunku wiec 1 tez wywali a dropwhile nie bo dropwhile zaczelo dzialac od jkaiegos momentu
for each in result:
    print(each)
print('-'*100)
months = ['Jan','Feb','Mar']
result = itertools.islice(months,0,2) # islice wytnie elemetny pomiedzy 10 a 2 czyli zacznij od elem 0 i skoncz na elem 2 ale drugiego juz nei pokaze
for e in result:
    print(e)
print('-'*100)
spades = ['Hearts','Tiles','Clovers', 'Pikes']
figuers = ['Ace','King', 'Queen', 'Jack', '10', '9'] # iloczyn kartezjanski czyli kazdy element z jednego zbioruu laczy nam z kazdym elementem z drugiego
result = itertools.product(spades,figuers)
for e in result:
    print(e)
print('-'*100)
for i in itertools.repeat('Tell me more',2): # powtarza w kołko drugi argument mowi ile razy ma byc powtorzenie bez tego bedzie niskonczona petla
    print(i)
print('-'*100)
data = [(1,2),(3,4)]
result = itertools.starmap(operator.add, data) # starmap  nalezy wskazac operator jaki ma byc zastosowany wobec danych oraz obiekt z ktorych ma te dane brac  operator add pracuje na dwoch argumentach dlatego mamy tuple dwuelementwy
#add nie zadziala przy 3 i wiecej elementowych obiektach
for e in result:
    print(e)
print('-'*100)
cars = ['Ford','Opel','Toyota','Skoda']
cars1, cars2 = itertools.tee(cars) # tee pozwla stworzyc 2 iteratory niezalezne i mozna niezaleznie przejsc przez oba iteratory tego samego obiektu
for e in cars1:
    print(e)
for e in cars2:
    print(e)
print('-'*100)
months = ['Jan','Feb','Mar']
plan = ['busy','free']
result = itertools.zip_longest(months,plan,fillvalue='unknown') # pozwala polaczyc dwie listy i elementom z brakiem odpowiednika dac jakis napis fillvalue
for e in result:
    print(e)
