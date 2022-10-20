lista = list(range(10))
print(lista)

nowa = [i * 2 for i in lista] # birze liste, kazdy argument traktuje jako zmienną i i wykonuje dla i dzialanie
nowa2 = [i + 2 for i in lista if i % 2 == 0] # dodalismy warinek zeby wykonalo dzialnie tylko na parzystych
print(nowa)
print(nowa2)

# formatowanie String
argumenty = ["Filip", 32]
tekst = "Hello i am {0} and i am {1} years old.".format(argumenty[0], argumenty[1]) # w tekscie zostawaimy indeksy w klamrach gdzie po kropce funkcja format pod te indeksy mozemy przypisac jakies elementy z listy
print(tekst)
# mozna tez nazywac argumenty:
tekst2 = "Hello i am {imie} and i am {wiek} years old.".format(imie = argumenty[0],wiek = argumenty[1]) # w tekscie zostawaimy indeksy w klamrach gdzie po kropce funkcja format pod te indeksy mozemy przypisac jakies elementy z listy
print(tekst2)

