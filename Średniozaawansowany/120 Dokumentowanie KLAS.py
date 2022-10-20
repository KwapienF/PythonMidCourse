BrandOnSale = 'Kia'
# DOKUMENTOWANIE CZYLI KOMENTOWANIE WSZYSTKICH METOD CO ROBIA I OPISANIE ARGUMENTOW
class Car:
    """
    Car - class operatingon cars availbe in th edealer
    """
    numberofCars = 0
    listofCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK,isOnSale):  # konstruktor klasy init wywoluje si epo utowrzenie instancji klasy i init tylko porzadkuje dane wg wzorca
        """
        opisujemy co znaczą wszystkie argumenty
        :param brand:
        :param model:
        :param isAirBagOK:
        :param isPaintingOK:
        :param isMechanicOK:
        :param isOnSale:
        """
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale
        Car.numberofCars +=1 # definujemy tutaj bo init przechodzi po wszystkich instancjach wiec mamy pewnsoc ze bedzie tu tyle ile jest obiektow
        Car.listofCars.append(self)

    def isDamaged(self): # czy jest zniszczony sprawdzamy
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

    @classmethod # metoda dzialajaca na poziomie klasy
    def ReadFromText(cls,aText):
        aNewCar = cls(*aText.split(':')) # funckje split poprzedzamy giwzdka aby zwrocila nam konkretne wartosci bo bez gwiazki zwroci nam liste a jej ie chcemy w tym przykladzie
        return aNewCar

    #metoda statyczna: moze byc gdziekolwiek ale umieszczamy ja porzadnie w klasie
    @staticmethod
    def Convert_KM_KW(KM):
        return KM*0.735

    @staticmethod # metdoa nie przyjmuje self anic cls jest niezalzna od niczego
    def Convert_KW_KM(KW):
        return KW * 1.36

    ISONSALE = property(__GetIsOnSale,__SetisOnsale,None,'If set on true Car is availbe in SALE') # funkcja przyjmuj e 3 parametry 1 jaką funkcja pobieramy wartosc zmiennej, drugi jaka metoda ma byc uzywana do zmiany wartosci, 3 paramter moze usuanc element ale nie chcem yusuwac wiec none


car1 = Car('Seat','Ibiza', True, True, True,False)
car2 = Car('Kia','badziew', True, True, False,True)


lineOfText = 'Renault:Megan:True:True:False:False'
car3 = Car.ReadFromText(lineOfText) # dodwanie instanci za pomoca metody na poziomie klasy
car3.Getinfo()

help(Car) # pokazuej info wraz z komentarzami

