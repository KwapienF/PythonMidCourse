class Car: # definicja klasy
    numberofCars = 0
    listofCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):  # konstruktor klasy init wywoluje si epo utowrzenie instancji klasy i init tylko porzadkuje dane wg wzorca
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        Car.numberofCars +=1 # definujemy tutaj bo init przechodzi po wszystkich instancjach wiec mamy pewnsoc ze bedzie tu tyle ile jest obiektow
        Car.listofCars.append(self)

    def isDamaged(self): # czy jest zniszczony sprawdzamy
        return not (self.isAirBagOK, self.isMechanicOK, self.isPaintingOK)

    def Getinfo(self):
        print(f'{self.brand,self.model} Air bags are ok? ANSWER: {self.isAirBagOK}')


car1 = Car('Seat','Ibiza', True, True, True)
car2 = Car('KIA','badziew', True, True, False)

print(car1.brand,car1.model,car1.isDamaged(),car1.Getinfo())
print(car2.brand,car2.model,car2.isDamaged(),car2.Getinfo())
print('*'*40)
print('ID klasy: ',id(Car))
print('ID instancji, obiektów: ',id(car1),id(car2))
# id dowodzi ze klasa to co innego niz instancje itd

# mozna sprawdzic czy dana instancja obiekt pochdzoi czy tez nalezy do danej klasy
print(isinstance(car1,Car)) # czy instancja car1 nalezy do klasy Car
# innys psoob sprawdzenia czy obiekt nalezy do klasy
print(type(car1))
print(type(car1) is Car)
# kolejny sposób
print(car1.__class__)
print(car1.__class__ is Car)
# kolejny  sposbo pozwoli zobaczyc obiekt od srodka
print(vars(car1)) # sprawdzenie jakie atrybuty posaida dana instacnaj
print(vars(Car))


# funkcja dir - pokazuje cala zawartosc klasy czy obiektu nawet ukryte funkcje
print(dir(car1))
print(dir(Car))

print(car1.numberofCars) # mozna odwoalc sie do elementu klasy po przez instancje
