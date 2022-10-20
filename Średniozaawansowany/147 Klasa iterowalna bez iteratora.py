import datetime as dt

class Miliondaysiterator: # tworzymy klase iteratora dla miliondays aby uzdrowic klase miliondays bo wywalilismy znie metode next
    def __init__(self,date,max):
        self.date = date
        self.maxdays = max
    def __next__(self):
        if self.maxdays <=0:
            raise  StopIteration
        ret = self.date
        self.maxdays -= 1
        self.date += dt.timedelta(days=1)
        return ret
    # def __iter__(self): tego nie trzeba dawac
    #     return self


class Miliondays: # klasa posaida iterator na zewnatrz
    def __init__(self,year,month,day,maxdays):
        self.date = dt.date(year,month,day)  # tworzymy startowa date od ktorej rozpoczniemy iterowanie
        self.maxdays = maxdays
        self.iterator =Miliondaysiterator(self.date,self.maxdays)



    def __iter__(self): # w iter odwolujemy sie nie do klasy tylko do instancji iteratora przekazanego z klasy miliondaysiterator
        return self.iterator

md = Miliondays(2000,1,1,2500000)
# print(next(md)) nie uda sie bo musimy zrobic funkcje iter
print(next(iter(md)))
for d in md:
    pass