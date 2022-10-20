class pole_prostokata:
    def __init__(self):
        print("pole prostokąta")
    def czytaj_dane(self):
        self.a = float(input("Podaj bok a: "))
        self.b = float(input("Podaj bok b: "))
    def przetworz_dane(self):
        self.pole = self.a * self.b
        return self.pole
    def wynik(self):
        print("pole prostokąta wynosi: ", self.pole)
    def __del__(self):
        print("Koniec programu pamięć oczyszczona")
zadanie = pole_prostokata()
zadanie.czytaj_dane()
zadanie.przetworz_dane()
zadanie.wynik()





