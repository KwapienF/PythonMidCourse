

class Car:

    def __init__(self, brand, model,isOnSale):
        print('Car Class init starting')
        self.brand = brand
        self.model = model
        self.__isOnSale = isOnSale
        self.name = f'{brand} {model}'
        print('Car Class init finished')

    def Getinfo(self):
        print('Car Getinfoinit starting')
        super().Getinfo() # powoduje  to wywolanie metody u nastepnej klasy.  dodaje sie to aby wykonywanie nie urwalo sie tylko zrobilo swoje i rpzeszlo do nastepnej klasy
        print(f'{self.brand,self.model}')
        print("Is on Sale",self.__isOnSale)
        print('Car Getinfo init finished')

class Specialist: # specjalista, który zajmuje sie danymi autami
    def __init__(self, firstname, lastname,brand):
        print('Specialist Class init starting')
        self.firstname =firstname
        self.lastname = lastname
        self.name = "{} {}".format(firstname,lastname)
        self.brand = brand
        print('Specialist Class init finished')

    def Getinfo(self):
        print('Specialist Class init starting')
        print('{} {} - ({})'.format(self.firstname,self.lastname,self.brand))
        print('Specialist Class init finished')

class CarSpecialist(Car,Specialist):
    def __init__(self, brand, model,isOnSale,firstname,lastname):
        print('CarSpecialist Class init starting')
        Car.__init__(self, brand, model,isOnSale)
        Specialist.__init__(self, firstname, lastname,brand.upper()) # brand duzymi aby rozroznic
        print('CarSpecialist Class init finished')
    def Getinfo(self):
        print('CarSpecialist Class init starting')
        super().Getinfo()
        print('CarSpecialist Class init finished')

tom = CarSpecialist('Toyota','Corolla',True,'Tom','Smith')
print(vars(tom))
tom.Getinfo()
#aby zobaczyc jaka jest kolejnosc wywolywania poszcegolnych metod
print(CarSpecialist.__mro__) # metod resolution order
