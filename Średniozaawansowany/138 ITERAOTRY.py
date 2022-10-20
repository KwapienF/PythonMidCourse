# iterator to obiekt przez ktory mozna przejsc po kolei  iterrable
import datetime as dt
import sys

start = dt.datetime.now()
print(start)
# iterator to klasa funkcja ktora ma za zadanie zwraac nastepna wartosc

dates = [dt.date(2000,1,1) + dt.timedelta(days = i) for i in range (2500000)]
print('Size of dates is {} MB'.format(sys.getsizeof(dates)/1000000)) # getsizeof od sysy pokaze nam ile zajmuje pamieci operacyjnej
for d in dates: # przejscie przez liste
    pass
stop = dt.datetime.now()
print(stop)
print('Total time: ',stop-start)






print('TO SAMO ALE Z ZASTOSOWANIE ITERATOROW' * 10)

start1 = dt.datetime.now()
print(start1)

class Miliondays:
    def __init__(self,year,month,day,maxdays):
        self.date = dt.date(year,month,day)  # tworzymy startowa date od ktorej rozpoczniemy iterowanie
        self.maxdays = maxdays

    def __next__(self): # funkcja, którą wywola iteraotr kiedy bedzie prosil o kolejną wartość
        if self.maxdays <= 0:
            raise StopIteration()
        ret = self.date
        self.maxdays -= 1
        self.date += dt.timedelta(days = 1)
        return ret
    def __iter__(self): # ta funkcja powoduje ze zwrocimy iterator czyli cos co zawiera metode next dajemy self bo juz ta klasa ma next
        return self

md = Miliondays(2000,1,1,2500000)
# print(next(md))
# print(next(md))
# print(next(md))
# for i in range(2500000):
#     next(md)
print('Size of md is {} bajtów'.format(sys.getsizeof(md)))
for d in md:
    pass

stop1 = dt.datetime.now()
print(stop1)
print('Total time: ',stop1-start1)