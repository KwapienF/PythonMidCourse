from random import randint # ze zbioru random zaimportuj randint zbiór liczb losowych
#for i in range(100):  # pętla for dla danej zmiennej tutaj i przebiega określoną ilość razy
#    print(randint(1,10))  # liczba w nawiasie z lewej okresla od jakiej liczby najmniejszej do jakiej w nawiasie prawej ma wybierac liczby
# czyli wydrukowało nam 100 razy  liczbe  losową od 1 do 10
los = randint(1,100)
odp = -1
i = 0
print("Zgadnij liczbę z przedziału 1-100")

while odp != los: # pętla ma tak długo się wykonywać dopóki  odpowiedz jest różna od liczby wylosowanej
    i += 1
    odp = int(input("Zgadnij liczbę: "))
    if odp < los and odp < 100 and odp > 0:
        print(f"NIE! Ta  liczba jest większa. Próbuj dalej.")
    elif 0 >= odp or odp > 100:
        print("Z przedziału od 1 do 100 debilu!")
    elif odp > los:
        print(f"NIE! Ta  liczba jest mniejsza. Próbuj dalej.")
print(f"BRAWO!!! Zgadłeś liczbę :) zajęło ci to {i} prób.")



