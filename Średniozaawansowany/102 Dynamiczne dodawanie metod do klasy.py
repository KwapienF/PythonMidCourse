import csv
BrandOnSale = 'Kia'
import types # modul ktory pozwoli nam przypisac zewnetrzna funkcje do klasy taka by argumnet cls pobierala sobie sama bo bez tego wywali blad ze nie ma cls argumentu
def exporttofilestatic(path,header,data):
    with open(path,mode='w') as file: # otwarcie pliku do zapisu
        writer = csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL) # writer deklaruje jak pracowac z plikiem csv wskazuje z jakim plikiem ma pracowac, wrtosci maja byc rozdzielone przecunkiem
        # a jezeli jest wartosc ktora ma w sobie przecinek to takie wartosci oddzilic ma qutoechar  znakiem cudzyslowiu
        # quoting okresla jak mocno maja byc cytowane wszystkie wartosci, minimal oznacza ze wyswietli w cudzyslowiu tylko te wartosci ktore gdzies w srodku zawieraly przecinek a wartosci bez przecinka beda bez cudzyslowia
        writer.writerow(header) # zapiujemy naglowek, writerow zapis do pliku
        writer.writerow(data) # zapisujemy dane
    print('This is function export to file static method')
# robimy funckje eksportujacą dla klasy aby eksprotowala nam wszystkie instancje łatwo
def exporttofile_Class(cls,path): # robimy funkcje na poziomie klasy stad cls jako peirwszy argument
    with open(path,mode='w') as file: # otwarcie pliku do zapisu
        writer = csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL) # writer deklaruje jak pracowac z plikiem csv wskazuje z jakim plikiem ma pracowac, wrtosci maja byc rozdzielone przecunkiem
        writer.writerow(['Brand','Model','IsonSale'])
        for c in cls.listofCars:
            writer.writerow([c.brand,c.model,c.ISONSALE])
    print('This is function export to file CLASS method')
# i 3 rodzaj funckji czyli funkcja na poziomie instancji:
def exporttofile_Instance(self,path):
    with open(path,mode='w') as file: # otwarcie pliku do zapisu
        writer = csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL) # writer deklaruje jak pracowac z plikiem csv wskazuje z jakim plikiem ma pracowac, wrtosci maja byc rozdzielone przecunkiem
        writer.writerow(['Brand','Model','IsonSale'])
        writer.writerow([self.brand,self.model,self.ISONSALE])
    print('This is function export to file INSTANCE method')


class Car: # definicja klasy
    numberofCars = 0
    listofCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK,isOnSale):  # konstruktor klasy init wywoluje si epo utowrzenie instancji klasy i init tylko porzadkuje dane wg wzorca
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale
        Car.numberofCars +=1 # definujemy tutaj bo init przechodzi po wszystkich instancjach wiec mamy pewnsoc ze bedzie tu tyle ile jest obiektow
        Car.listofCars.append(self)

    def isDamaged(self): # czy samochod  jest zniszczony sprawdzamy
        return not (self.isAirBagOK, self.isMechanicOK, self.isPaintingOK)

    def Getinfo(self):
        print(f'{self.brand,self.model} Air bags are ok? ANSWER: {self.isAirBagOK}')
        print("Is on Sale",self.__isOnSale)

    def __GetIsOnSale(self): # ukrywamy funkcje bo dla nich zdefiniowana jest wlasciwosc
        return self.__isOnSale
    def __SetisOnsale(self,newIsOnSaleStatus):
        if self.brand == BrandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('CHanging status is nasale to ',newIsOnSaleStatus)
        else:
            print('Cannont Change status isonsale')



    ISONSALE = property(__GetIsOnSale,__SetisOnsale,None,'If set on true Car is availbe in SALE') # funkcja przyjmuj e 3 parametry 1 jaką funkcja pobieramy wartosc zmiennej, drugi jaka metoda ma byc uzywana do zmiany wartosci, 3 paramter moze usuanc element ale nie chcem yusuwac wiec none


car1 = Car('Seat','Ibiza', True, True, True,False)
car2 = Car('Kia','badziew', True, True, False,True)
print('Static'*10)
Car.Exporttofilestatic = exporttofilestatic # dzieki temu implementujemy funkcje zewnetrzna w klase
#exporttofilestatic(r'C:\temp\export_static.csv',['Brand','Model','IsonSale'],[car1.brand,car1.model,car1.ISONSALE])
Car.Exporttofilestatic(r'C:\temp\export_static.csv',['Brand','Model','IsonSale'],[car2.brand,car2.model,car2.ISONSALE])
print(dir(Car))

#Car.Exporttofile_Class = exporttofile_Class# tak nie przypisujemy funkcji zewnetrznej do funkcji na poziome kasy trzeba zrobic to modulem type jak nizej:
Car.Exporttofile_Class = types.MethodType(exporttofile_Class,Car) # jaka funckja do jakiej klasy ma byc przypisana
Car.Exporttofile_Class(path=r'C:\temp\export_CLASS.csv')
car1.Exporttofile_Instance = types.MethodType(exporttofile_Instance,car1) # funkcja na poziome instancji dlatego przypsiujemy ja do instancji a nie do klasy
car1.Exporttofile_Instance(path=r'C:\temp\export_Instance.csv')
print(dir(car1))

# jak sprwadzic czy dana instancja ma metode czy atrybut?
print('-'*50)
if hasattr(car1,'Exporttofilestatic') and callable(car1.Exporttofilestatic):
    print('The object has method exporttofilestatic')
#hasattr sprwadza czy istnieje atrybut dl anazwy funkcji jaka chce sprawdzic dla danego obiektu, sprawdz czy nazwa w'' jest w klasie ale wciaz nei swiadczy o tym ze jest ta nazwa funkcja dlatego dalej:
# callable sprawdza czy tą nazwe mozna uruchomic jako funkcję?



