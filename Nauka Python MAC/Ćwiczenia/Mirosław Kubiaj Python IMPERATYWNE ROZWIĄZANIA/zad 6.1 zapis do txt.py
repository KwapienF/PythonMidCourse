def txt():
    file = open("/Users/filipkwapien/Desktop/zadanie6.1.txt", "w")
    imie = file.write(input("Podaj imię: " + "\n",))
    file.write(" ")
    nazwisko = file.write(input("Podaj nazwisko: " + "\n"))
    print("Dziękuję")
    file.close()

    # otwarcie pliku i zczytanie danych
    file = open("/Users/filipkwapien/Desktop/zadanie6.1.txt", "r")
    #text = file.readlines() wyswietli jako liste elementy tekstu
    text = file.read() #wyświetli tekst ładnie a nie jako liste w nawiasach kwadratowych
    print(text)
txt()