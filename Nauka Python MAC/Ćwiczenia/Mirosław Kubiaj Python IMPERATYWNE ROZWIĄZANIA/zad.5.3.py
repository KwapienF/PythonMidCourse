import random
class Tablica():
    def __init__(self):
        print("Tablica 10x10 z losowymi liczbami po przekątnej sumującymi się")
    def __del__(self):
        print("Koniec programu")
        print("Zwolnienie pamięci")
    def create_an_array(self,n,rozmiar):
        self.i = rozmiar
        self.row =[]
        self.n = n
        self.los = random.randint(0, 9)
        for i in range(self.i):
            if i == n:
                self.row.append(self.los)
            else:
                self.row.append(0)
        print(self.row)
    def suma(self):
        return self.los
def main():
    program = Tablica()
    n = 0
    w = 0
    rozmiar = int(input("Podaj rozmiar tablicy: "))
    for j in range(0, rozmiar):
        program.create_an_array(n,rozmiar)
        w += program.suma()
        n += 1
    print("Suma liczb po przekątnej wynosi: ",w)
main()










