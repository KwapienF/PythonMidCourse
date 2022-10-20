class KontoBankowe:
    __stan = 0  # utrudnienei dostepu do zmiennej stan __ prywatne ale nie do konca bo to python

    @property # właściwość  i wtedy funkcja nie jest odczytywane jako funkcja a jako zmienna
    def stan_konta(self):
        return self.__stan
    #gettery i settery tworzymy tylko dla wlsciwosci
    #getter pobiera dane
    @stan_konta.getter
    def stan_konta(self):
        return "Stan konta: " + str(self.__stan) + " zł" # wyswietli geter przy uruchomieniu bo getter ma priorytet a nazwa taka sama wlsciwosci i getter
    @stan_konta.setter
    def stan_konta(self, value):
        self.__stan += value # setter dodane srodki doda nam do konta

konto = KontoBankowe()
print(konto.stan_konta) # bez nawiasow na koncu bo wlasciowjsc property. bez tego by trzebabylo dac nawiasy na koncu ()
#konto.stan_konta = 50 # nie mozna przypisywac nowej danej  bo wlasciwosc jest stala tylko do odczytu
konto.stan_konta = 50
print(konto.stan_konta)
konto.stan_konta = 100
print(konto.stan_konta)
konto.stan_konta = -75
print(konto.stan_konta)