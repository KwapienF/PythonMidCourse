import pickle
class Osoba:
    def __init__(self):
        print("Star programu")
    def czytaj_dane(self):
        self.nazwisko = input("Nazwisko: ")
        self.imie = input("Imie: ")
        self.ulica = input("Ulica: ")
        self.dane = self.nazwisko + self.imie + self.ulica
        print()
    def zapisz_dane_do_pliku(self):
        with open("/Users/filipkwapien/Desktop/Plik.binarny", "wb") as plik1:
            pickle.dump(self.dane, plik1)
    def czytaj_dane_z_pliku(self):
        with open("/Users/filipkwapien/Desktop/Plik.binarny", "rb") as plik2:
            self.dane1 = pickle.load(plik2)
def main():
    pracownik = Osoba()
    pracownik.czytaj_dane()
    pracownik.zapisz_dane_do_pliku()
    print("Zapisano dane")
    pracownik.czytaj_dane_z_pliku()
    print("zczytano dane")
main()