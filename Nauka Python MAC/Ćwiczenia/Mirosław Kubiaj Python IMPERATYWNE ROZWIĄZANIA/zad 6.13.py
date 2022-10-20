import pickle
def main():
    daneksiazki = [] # pusta lista
    daneksiazek = {} # pusty slownik

    daneksiazki.append(input("Imię autora: "))
    daneksiazki.append(input("Nazwisko autora: "))
    daneksiazki.append(input("tytuł : "))
    daneksiążek = {1: daneksiazki}

    print(daneksiążek)
    with open("/Users/filipkwapien/Desktop/Plik.binarny1", "wb") as plik1:
        pickle.dump(daneksiążek, plik1)


    with open("/Users/filipkwapien/Desktop/Plik.binarny1", "rb") as plik2:
        dane1 = pickle.load(plik2)
    print(dane1)
main()