import math
class trojmian:
    def __init__(self):
        self.a = float(input("Podaj a: "))
        self.b = float(input("Podaj b: "))
        self.c = float(input("Podaj c: "))
    def __del__(self):
        print("Koniec programu, zwolnienie pamięci")
    def delta(self):
        self.delta = self.b**2 -4 * self.a * self.c
        return self.delta
    def delta_dodatnia(self):
        print("Równanie ma 2 pierwiastki: ")
        self.x1 = (-self.b - math.sqrt(self.delta))/(self.a * 2)
        self.x2 = (-self.b + math.sqrt(self.delta))/(self.a * 2)
        print("x1: ", round(self.x1, 2)," oraz x2: ", round(self.x2,2))
    def deltla_zerowa(self):
        print("Równanie ma 1 pierwiastek: ")
        self.x0 = (-self.b)/(2 * self.a)
        print("x0: ", round(self.x0, 2))
    def delta_ujemna(self):
        print("Brak pierwiastków, delta ujemna")
object = trojmian()
def main():
    if object.delta() > 0:
        object.delta_dodatnia()
    elif object.delta == 0:
        object.deltla_zerowa()
    else:
        object.delta_ujemna()
main()


