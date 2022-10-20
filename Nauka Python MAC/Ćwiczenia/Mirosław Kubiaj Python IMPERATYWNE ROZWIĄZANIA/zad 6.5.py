import os
workers_number = int(input("Lista zatrudnionych pracowników: "))
def main():
    file = open("/Users/filipkwapien/Desktop/pracownicy.txt", "w+")
    i = 1
    while i <= workers_number:
        nr = (f"pracownik numer {i}" + "\n")
        file.write(nr)
        imie = input("Imię pracownika: ")
        file.write("imię pracownika: " + imie + "\n")
        stanowisko = input("Stanowisko pracownika: ")
        file.write("Stanowisko: " + stanowisko + "\n")
        i += 1
    file = open("/Users/filipkwapien/Desktop/pracownicy.txt", "r")
    if file.readable():
        tekst = file.read()
        tekst = tekst.rstrip("\n")

def main1():
    file = open("/Users/filipkwapien/Desktop/pracownicy.txt", "a")
    workers_number2 = int(input("Podaj liczbę nowozatrudnionych pracowników: "))
    i = 1
    while i <= workers_number2:
        nr = (f"pracownik numer {i + workers_number}" + "\n")
        file.write(nr)
        imie = input("Imię pracownika: ")
        file.write("imię pracownika: " + imie + "\n")
        stanowisko = input("Stanowisko pracownika: ")
        file.write("Stanowisko: " + stanowisko + "\n")
        i += 1
    file = open("/Users/filipkwapien/Desktop/pracownicy.txt", "r")
    if file.readable():
        tekst = file.read()
        tekst = tekst.rstrip("\n")
main()
print("Czy chcesz wprowadzić kolejnego pracownika? wpisz tak lub nie")
decyzja = input("Tak czy nie?: ".lower())
if decyzja == "tak":
    main1()
else:
    print("Dziękujemy za wprowadzenie nowych pracowników")

def modify():
    a = input("Podaj imię i nazwisko, które chcesz zmienić: ")
    szukaj = (f"imię pracownika: {a}")
    prac_plik = open("/Users/filipkwapien/Desktop/pracownicy.txt", "r")
    temp_file = open("/Users/filipkwapien/Desktop/zmodyfikowany.txt", "w")
    dane = prac_plik.readline()  # odczytujemy pole pierwszego rekordu
    while dane != "":  # odczytuje kolejne pola
        ident = prac_plik.readline()
        dzial = prac_plik.readline()

        dane = dane.rstrip("\n")
        ident = ident.rstrip("\n")
        dzial = dzial.rstrip("\n")

        if ident == szukaj:
            nowe_dane = input("Podaj nowe  dane pracownika: ")
            temp_file.write(dane + "\n")
            temp_file.write("imię pracownika: " + nowe_dane + "\n")  # zapisuje zmodyfikowany rekord w pliku tymczasowym
            temp_file.write(dzial + "\n")
        else:
            temp_file.write(dane + "\n")
            temp_file.write(ident + "\n")
            temp_file.write(dzial + "\n")
        dane = prac_plik.readline()
    prac_plik.close()
    temp_file.close()

print("Czy chcesz zmodyfikować pracownika?")
decyzja2 = input("Tak czy nie?: ".lower())
if decyzja2 == "tak":
    modify()
else:
    print("Zakończono pracę")

def erase():
    a = input("Podaj imię i nazwisko, którego chcesz usunąć: ")
    szukaj = (f"imię pracownika: {a}")
    prac_plik = open("/Users/filipkwapien/Desktop/zmodyfikowany.txt", "r")
    temp2_file = open("/Users/filipkwapien/Desktop/usunięty.txt", "w")
    dane = prac_plik.readline()  # odczytujemy pole pierwszego rekordu
    while dane != "":  # odczytuje kolejne pola
        ident = prac_plik.readline()
        dzial = prac_plik.readline()

        dane = dane.rstrip("\n")
        ident = ident.rstrip("\n")
        dzial = dzial.rstrip("\n")
        if ident == szukaj:
            temp2_file.write("")
            temp2_file.write("")  # zapisuje zmodyfikowany rekord w pliku tymczasowym
            temp2_file.write("")
        else:
            temp2_file.write(dane + "\n")
            temp2_file.write(ident + "\n")
            temp2_file.write(dzial + "\n")
        dane = prac_plik.readline()
    prac_plik.close()
    temp2_file.close()
print("Czy chcesz usunąć pracownika?")
decyzja2 = input("Tak czy nie?: ".lower())
if decyzja2 == "tak":
    erase()
else:
    print("Zakończono pracę")


















