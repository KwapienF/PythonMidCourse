class Car: # definicja klasy

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):  # konstruktor klasy init wywoluje si epo utowrzenie instancji klasy i init tylko porzadkuje dane wg wzorca
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
    def isDamaged(self): # czy jest zniszczony sprawdzamy
        return not (self.isAirBagOK, self.isMechanicOK, self.isPaintingOK)

    def Getinfo(self):
        print(f'{self.brand,self.model} Air bags are ok? ANSWER: {self.isAirBagOK}')


car1 = Car('Seat','Ibiza', True, True, True)
car2 = Car('KIA','badziew', True, True, False)


print(car1.brand,car1.model,car1.isDamaged(),car1.Getinfo())
print(car2.brand,car2.model,car2.isDamaged(),car2.Getinfo())
