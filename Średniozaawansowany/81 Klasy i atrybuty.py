class Car: # definicja klasy

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):  # konstruktor klasy init wywoluje si epo utowrzenie instancji klasy i init tylko porzadkuje dane wg wzorca
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

car1 = Car('Seat','Ibiza', True, True, True)
car2 = Car('KIA','badziew', True, True, False)

print(car1.brand,car1.model)


# programowanie proceduralne  to takie gdzie funckje sa oddzielnie i zmienne sa oddzielnie. Klasa to ogolny opis a w opraciu o klase powstaje instancja klasy czy obiekt czyli szcegolowe  juz okreslenie konkretnych parametrów





