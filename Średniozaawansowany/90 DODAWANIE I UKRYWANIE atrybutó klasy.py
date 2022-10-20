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


car1 = Car('Seat','Ibiza', True, True, True,False)
car2 = Car('KIA','badziew', True, True, False,True)

print(car1.brand,car1.model,car1.isDamaged(),car1.Getinfo())
print(car2.brand,car2.model,car2.isDamaged(),car2.Getinfo())
print('*'*40)

# moge zmienic ins ons ale z zewnatrz poleceniem:
car2.__isOnSale = False
print(vars(car2)) # i zmienilo si ena False mimo ze mial byc w promocji a tego nie chcemy
# dlatego trzeba ten paramter ukryc ay nikt po za nami nie mogl go zmienic. Robimy to dodajdac dwie podlogi przed atrybutem czuli __isOnSale
# samochod nie zmieni sie czy jest onsale czy nie.

# mozna to oebscj  definujac zmiane z klasą czyli _Car__isOnSale = False wtedy oszukamy Klase i zmienimy

# mzona dodac atrybut do kalsy:
car2.YearofProduction = 2005
print(vars(car2))
# mozna tez usunac atrybut
del car2.YearofProduction
print(vars(car2))

# modyfikowanie atrybutów:
setattr(car2,'TAXI',False) # co modyfikujemy, jaki dodajemy atrybut i jaka wlasciwoac ma ten atrybut
print(vars(car2))

print(hasattr(car2,'TAXI')) # funkcja ta sprawdza czy dany obeikt posiada atrybut o konkretnej nazwie

# inny spsoob na usuniecie atrybutu:
delattr(car2,'TAXI')
print(vars(car2))