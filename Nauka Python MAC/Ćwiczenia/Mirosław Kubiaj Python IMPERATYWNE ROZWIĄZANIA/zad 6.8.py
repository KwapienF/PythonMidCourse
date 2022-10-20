import os
def main():
    znaleziony = False
    a = input("Podaj imię i nazwisko, które chcesz zmienić: ")
    szukaj = (f"imię pracownika: {a}")
    prac_plik = open("/Users/filipkwapien/Desktop/pracownicy.txt", "r")
    temp_file = open("/Users/filipkwapien/Desktop/tymczasowy.txt", "w")
    dane = prac_plik.readline() # odczytujemy pole pierwszego rekordu
    while dane != "": #odczytuje kolejne pola
        ident = prac_plik.readline()
        dzial = prac_plik.readline()

        dane = dane.rstrip("\n")
        ident = ident.rstrip("\n")
        dzial = dzial.rstrip("\n")

        if ident == szukaj:
            nowe_dane = input("Podaj nowe  dane pracownika: ")
            temp_file.write(dane + "\n")
            temp_file.write("imię pracownika: " + nowe_dane + "\n") # zapisuje zmodyfikowany rekord w pliku tymczasowym

            temp_file.write(dzial + "\n")
            found = True
        else:
            temp_file.write(dane + "\n")
            temp_file.write(ident + "\n")
            temp_file.write(dzial + "\n")
        dane = prac_plik.readline()
    prac_plik.close()
    temp_file.close()

main()

