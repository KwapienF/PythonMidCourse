BrandOnSale = 'Kia'

class Car: # definicja klasy


    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK,isOnSale):  # konstruktor klasy init wywoluje si epo utowrzenie instancji klasy i init tylko porzadkuje dane wg wzorca
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale

    #def __GetIsOnSale(self): # ukrywamy funkcje bo dla nich zdefiniowana jest wlasciwosc
    #    return self.__isOnSale

# nie ptrzebujemy juz przy takim zdefinowaniu wlasciwoscii powyzszej funkcji get
    #ISONSALE = property(__GetIsOnSale,__SetisOnsale,None,'If set on true Car is availbe in SALE') # funkcja przyjmuj e 3 parametry 1 jaką funkcja pobieramy wartosc zmiennej, drugi jaka metoda ma byc uzywana do zmiany wartosci, 3 paramter moze usuanc element ale nie chcem yusuwac wiec none
    @property
    def ISONSALE(self):
        return self.__isOnSale

# musi byc funckja za wlasciwoscia bo ja dekorujemy ta wlasciwoscia

    @ISONSALE.setter  # dzieki temu wlasciwosc opisana w ISONSALE bedziemy mogli modyfikwoac tą funkcja. Bez tego nie mozemy modyfikowac i ta funckja msui miec nazwe taka  jak wlasciowsc
    def ISONSALE(self, newIsOnSaleStatus):
        if self.brand == BrandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('CHanging status isonsale to ', newIsOnSaleStatus)
        else:
            print('Cannont Change status isonsale for this model')
    @ISONSALE.deleter # pozwoli usuwac nam atrybuty
    def ISONSALE(self):
        self.__isOnSale = None

    @property # ta wlasciowsc pozwoli nam wyswietlic dane o samochdozie marce i mdoelu
    def Cartitle(self):
        return(self.brand,self.model)



car1 = Car('Seat','Ibiza', True, True, True,False)
car2 = Car('Kia','badziew', True, True, False,True)

print(car1.ISONSALE)# ISONSALE bez nawaisow na koncu() bo zdefuniwalismy jako property czyli wlasciwosc
#car1.ISONSALE = True # bedzie blad nie mozna zmienic
car1.ISONSALE = True
del car1.ISONSALE
print(car1.ISONSALE) # wywali none bo usunelismy atrybut
print(car2.Cartitle)


