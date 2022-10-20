BrandOnSale = 'Kia'

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

    ISONSALE = property(__GetIsOnSale,__SetisOnsale,None,'If set on true Car is availbe in SALE') # funkcja przyjmuj e 3 parametry 1 jaką funkcja pobieramy wartosc zmiennej, drugi jaka metoda ma byc uzywana do zmiany wartosci, 3 paramter moze usuanc element ale nie chcem yusuwac wiec none


car1 = Car('Seat','Ibiza', True, True, True,False)
car2 = Car('Kia','badziew', True, True, False,True)

print(car1.brand,car1.model,car1.isDamaged(),car1.Getinfo())
print(car2.brand,car2.model,car2.isDamaged(),car2.Getinfo())


print('-'*50)
car1.ISONSALE = True
print(car1.ISONSALE)
