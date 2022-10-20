class Test:
    def __new__(cls): # metoda new jest wykonywanan zawsze gdy tworzymy nowy obiekt hierarchia init potem new ale tu dla przyklady ze takie cos jest
        print("Hello Class")
obiekt = Test()

class Test2:
    def __del__(self):
        print("Bye Class")# desrtuktor czyli co ma sie wykonac kiedy klasa konczy swoja zywotnosc oczyszcza iz walnia pamiec programu
# del zawsze wykonywana jest zawsze na sam koniec programu czyli by class wyswielti sie po ostatniej linijce kodu jak np print koniec
obiekt2 = Test2() # instancja klasyc zyli wtedy kiedy klasa przeradza sie w obiekt
obiekt = obiekt2 # mozna odwolac sie do obiektu przed jego zniszczeniem ale po juz nie
del obiekt2 # usuwa nam niepotrzebny obiekt lub tez mozna usunac takie zmienna cokolwiek I wtedy destruktor wykona swoje zdanie  przed usunieciemm danej klasy

print("Koniec")

