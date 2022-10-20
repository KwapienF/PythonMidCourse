plik = open("/Users/filipkwapien/Desktop/test.txt","a")  # w oznacza write i pozwala nam otworzyc plik do zapisu, edycji a bez tego byłby tylko do odczytu
#plik utowrzy sie domyslnie w folderze co plik pythona chyba, ze podamy sciezke pelną gdzie ma go zapisac
if plik.writable():# funkcja writable daje namw artos true jezeli plik jest w stanie do zapisu, a do odczytu false do odczytu definiujemy przez "r"
    ile = plik.write(input("Wprowadź tekst: ") + "\n") # write pozwala nam dodac ciag string dp pliku
    print("zapisano: ", ile) # zmianna ile pokaze nam liczbe ile zapisany tekst mial bajtów czyli np dla 123456 ma 7 bajtow bo 6 znakow + ukosnik nowej lini \n tez liczy jako bajt
plik.close() # zamykamy  plik aby zwolnił pamięć

# teraz wyswietlimy to co zapisuje sie w pliku txt na ekranie konsoli aby nie sprawdzac caly czas pliku txt tryb do odczytu i zapisu jednoczesnie to "w+"
plik = open("/Users/filipkwapien/Desktop/test.txt", "r")
if plik.readable():
   # tekst = plik.read()  #Funkcja read zwraca tekst pliku
    tekst = plik.readlines() # zczytuje tam cale lienie z kodu i wyswietla jej elementy jako listę
    print(tekst)
    for l in tekst: # petla for teraz wyswietli nam wszystkie elementy z listy
       print(l) # duze odstepy w wyniku bo \l daje nowa linie i funkcja print sama w sobie tez nowa ale wyswietla sie w txt jedna
    # "w"  zapisuje nam caly czas od nowa, aby wprowadzony tekst wczesneij sie zachowywal a nowy dodawal trzeba uzyc "a" append
# inny sposób na wyswietlenie linijak po linijce zawartosci pliku
# if plik.readable():
#     for plik.readable():
#         print("zawartosc pliku:")
#         for l in plik:
#             print(l)


# KODOWANIE POLSKICH ZNAKÓW:  open("test.txt,'a',encoding='utf-8')