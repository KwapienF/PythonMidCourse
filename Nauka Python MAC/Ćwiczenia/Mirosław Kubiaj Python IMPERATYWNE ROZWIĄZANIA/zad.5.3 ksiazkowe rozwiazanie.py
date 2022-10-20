import random
class Tablica1:
    def __init__(self):
        print("Tablica 10x10 z losowymi liczbami po przekątnej sumującymi się")
    def __del__(self):
        print("Koniec programu")
        print("Zwolnienie pamięci")
    def create_an_array(self, N, tablica): # metoda zapelniająca tablice
        for i in range(N):
            for j in range(N):
                liczba = random.randint(1,9)
                if i == j:
                    tablica[i][j] = liczba
                else:
                    tablica[i][j] = 0
        for i in range (N):
            for j in range(N):
                print(tablica[i][j], " ", end = "")  # wyświetla liste
            print()
    def oblicz_sume(self, N, tablica):
        suma = 0
        for i in range(N):
            suma += tablica[i][i]
        print("Suma = ", suma)
def main():
    N = int(input("Podaj rozmiar tablicy: "))
    tablica = [[0 for i in range(N)] for j in range(N)] # generator zagnieżdżony tworzy maciesz NxN wypelniona zerami
    macierz = Tablica1()
    macierz.create_an_array(N, tablica)
    macierz.oblicz_sume(N, tablica)
    del macierz
main()





