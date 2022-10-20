import random
file = open("/Users/filipkwapien/Desktop/zadanie6.3.txt", "w+")
class Tablica():
    def __init__(self):
        file.write("Tablica 10x10 z losowymi liczbami po przekątnej sumującymi się" + "\n")
    def __del__(self):
        file.write("Koniec programu" + "\n")
        file.write("Zwolnienie pamięci" "\n")
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
        file.write(str(self.row) + "\n")

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
    file.write(f"Suma liczb po przekątnej wynosi: {w}" + "\n")
main()
file = open("/Users/filipkwapien/Desktop/zadanie6.3.txt", "r")
text = file.read()
print(text)
file.close()