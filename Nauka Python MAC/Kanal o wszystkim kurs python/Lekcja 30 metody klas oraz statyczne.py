class Czlowiek:
    def __init__(self, imie):
        self.imie = imie
    def przedstaw(self):
        print("Nazywam się: " + self.imie)
    # obiekty przechowuja metody a nie klasy wiec aby zadzialalo trzeba zdefuniowac obiekt jako klase i wywolya metody obiektem

    #metoda klasy:
    @classmethod # aby klasa przechowywala meotdy bez koniecznosci definiowana obeiktu
    def nowy_czlowiek(cls, imie ):  # w metodzie klasy nie ma self bo nie moze odwolac sie klasa do samej siebie bo obiekt nie istnieje jeszcze
        # cls odwoluje sie do klasy
        return cls(imie)  # cls = class zwraca imie w odwolaniu do klasy
    # metoda statyczna:
    @staticmethod
    def przywitaj(arg): # metody statyczne nie przyjmują pierwszego ukrytego argumentu
        print("Cześć " + arg + " !")
cz1 = Czlowiek.nowy_czlowiek("Filip") # nie tworzymy obiektu z cz1 robiac czlowiek(Filip) tylko korzystamy z metody klasy
cz1.przedstaw()
cz3 = cz1.nowy_czlowiek("Kwap")
cz3.przedstaw()
cz2 = Czlowiek("Lecia") # tutaj tworzymy obeikt a wyzej skorzystalismyz  metody klasy i obyla sie bez tworzenia obiektu
print(cz2.przedstaw())

Czlowiek.przywitaj("przyjacielu")
cz1.przedstaw()