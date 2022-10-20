import datetime as dt
# generator to funkcja wiec class zamieniamy na def. Generator to funckja ktora zwraca wartosc tylko wtedy kiedy o to prosimy
def Miliondays(year,month,day,maxdays):
    date = dt.date(year,month,day)
    for i in range(maxdays):
        yield(date + dt.timedelta(days = i)) # yield zwraca wartosc i zamraza funkcje ale kolejna wartosc zwroci jak sie znowu odwolay do niej a return przerwie funkcje czyli yeld zwraca wartosc i dziala dalej

for d in Miliondays(2000,1,1,5):
    print(d)

def Getmagicnumerbs():
    yield(22)
    yield(4)
    yield(5)

r = Getmagicnumerbs() # trzeba uzyc next aby wydobyc wartosc
# print(next(r))
# print(next(r))
# print(next(r))
#print(next(r)) # tu juz sie skonczy
# bez next mozna uzyc for
for n in r:
    print(n)
    # LAZY EVALUATION to generowanie wartosc wtedy kiedy je potrzebujemy a nie wszystkie naraz. Oszczedza to czas i pamiec