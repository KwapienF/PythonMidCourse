class Animal:  # tworzymy jakies zwierze
    def __init__(self, name, age):  # konstruktor
        self.name = name
        self.age = age
# chcemy utworzy klase psow oraz kotow zale zamiast osobno je tworzy mozna zrobic ze jedna jest psem a druga dziedziczy tresc ale robi kota
class Dog(Animal):  # w nawiasach podajemy klase ktorej funkcjonalnosc chcemy zaimplementowac
    def voice(self):
        print("Whuf! Whuf!")
class Cat(Animal):
    def voice(self):
        print("Meow Meow")
class Wolf(Dog): # dziedziczymy po psie
    def voice(self):
        print("Jestem wilkiem, ")
        super().voice()  # super szuka nam elementow  z klasy dziedziczonej tam zdefiniowanych czyli znajdzie nam voice od psa

dog = Dog("Reksio",10)  # tworzymy obiekt pies)
print(dog.name)
print(dog.age)
dog.voice()
cat = Cat("Murs", 12)
print(cat.name)
print(cat.age)
cat.voice()

wolf = Wolf("Geralt", 55)
wolf.voice() # supper odziedziczylo od psa odglos wiec nie musielismy w klasie wilk definiowac nowego glosu
print("Mam na imię " + wolf.name + " lat " + str(wolf.age))
