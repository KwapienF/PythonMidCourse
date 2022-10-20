class Car: # definicja klasy

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK,accesories):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.accesories = accesories


    def Getinfo(self):
        print(f'{self.brand,self.model} Air bags are ok? ANSWER: {self.isAirBagOK}')
        print(f'{self.brand, self.model} Painting ok? ANSWER: {self.isPaintingOK}')
        print(f'{self.brand, self.model} Mechanic ok? ANSWER: {self.isMechanicOK}')
        print(f'{self.brand, self.model} Air bags are ok? ANSWER: {self.isAirBagOK}')
        print(f'{self.brand, self.model} AAccesories: {self.accesories}')

    def __iadd__(self, other):  # iadd  znaczy +=   samo add to tylko +
        if type(other) is list:
            accesories = self.accesories
            accesories.extend(other) # extend dodaje listy do listy append dodaje string do listy :)
            return Car(self.brand,self.model,self.isAirBagOK,self.isPaintingOK,self.isMechanicOK,accesories)
        elif type(other) is str:
            accesories = self.accesories
            accesories.append(other) # extend dodaje listy do listy append dodaje string do listy :)
            return Car(self.brand,self.model,self.isAirBagOK,self.isPaintingOK,self.isMechanicOK,accesories)
        else:
            print('Please add string or list')
# dodawanie do siebie dwóch samochodów
    def __add__(self, other):
        if type(other) is Car:
            return[self,other]
        else:
            raise Exception('Adding type{} to Car is not implemented'.format(type(other)))
# ta funkcja pozwoli nam przedstawienie zawatosci instancji w postaci tekstu jak np wpiszemy print(car1) to nie wywali obiektu tylko tekst
    def __str__(self):
        return 'Brand: {}, Model: {}'.format(self.brand,self.model)



car1 = Car('Seat','Ibiza', True, True, True,['Winter Tires'])
car1.Getinfo()

car1 +=['Navigation','roof rack']
car1.Getinfo()
# jak zrobic aby dodawc elementy bez nawiasu kwadratowego?
car1 +='back camera'
car1.Getinfo()

car2 = Car('Opel','Corsa', True, True, True,[])
car_pack = car1 + car2
print('Car pack = ',car_pack[0].brand,car_pack[1].brand)
print(car1)