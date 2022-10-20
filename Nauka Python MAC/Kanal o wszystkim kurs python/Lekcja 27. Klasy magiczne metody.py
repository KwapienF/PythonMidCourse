import math
class Point2D: # bez nawiasow okraglych bo nawiasy dajemy wtedy kiedy chcemy odziedziyc cos z innej klasy
    def __init__(self, x, y): #metody magicnze to wszystkie metody ktore zaczynamy od __init__ one zacyznaja sie __ __
        self.x = x
        self.y = y
        self.distance0 = math.sqrt(x**2 + y**2) # odleglosc od srodka wspolrzednych
    def __add__(self, second): # dodawanie do siebie
        return Point2D(self.x + second.x, self.y + second.y) # bierze x z klasy i dodaje do niej x z drugiej klasy
    #def __sub__(self,second): #sub odejmowanie, mul mnozenie itd def dzielenie, mod reszta z dzielenia, pow potega
    def __lt__(self, second): # lt  operator mniejsze niz less then
        return self.distance0 < second.distance0
    def __eq__(self, second):  # mniejsze rowne less equak, eq rowne equal
        return self.x == second.x and self.y == second.y
    def __len__(self):
        return int(round(self.distance0, 0)) # round zaokragla nam do 0 po pzecinku i kowertujemy to na int
p1 = Point2D(2,5) # pkt z peirwszej klasy
p2 = Point2D(4,5) # pkt z drugiej klasy
p3 = p1 + p2
print(p3.x)
print(p3.y)
print(p1 < p2) # wyswietli true bo porwna dodalismy taka funkcjonalnosc do klasy mniejszy czyli blizszy srodka ukladu
print(p1.distance0)
print(p2.distance0)
print(p3 < p2)
print( p1 == p2)
print( p2 == p2)
print(len(p3))
print(p3.distance0)