import datetime as dt

class Miliondays:

    def __init__(self,year,month,day,maxdays):
        self.date = dt.date(year,month,day)  # tworzymy startowa date od ktorej rozpoczniemy iterowanie
        self.maxdays = maxdays
        #getitem zamiast next aby stworzyc funkcje generuyjace dalsze wartosci

    def __getitem__(self, item): # item paramter okresla ktora wartosc ma byc ma wygenerowana np 0 to pierwsza wartosc a item nr 3 to czwarta data z kolei
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration

md = Miliondays(2000,1,1,25)
print(md[0],md[1],md[2],md[3]) # mozna po indeksie sie odwolywac do wartosc
#print(next(md)) nie da sie bo nie ma next wiec nie ma iteratra ALE mozna to obejsc
it = iter(md)  #tworzymy iterator od danego obiektu  i mozna uzywac next

print(next(it))
print(next(it))
print(next(it))

for d in md:
    print(d)

