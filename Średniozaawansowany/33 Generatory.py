product = []
listA = list(range(6))
listB = list(range(6))

product = []
for a in listA:
    for b in listB:
        product.append((a,b))
# to samo w jednej lini
product = [(a,b)for a in listA for b in listB]
# aby wyswietlic nieparzyste w a i parzyste w listb
product = [(a,b)for a in listA for b in listB if a % 2 ==1 and b % 2 == 0]
# slownik
product = {a:b for a in listA for b in listB if a % 2 ==1 and b % 2 == 0}
 # w slowniku nadpisuja sie wartosci dla klucza dlatego mamy 1:4 w wyniu bo 1:0 zastapilo 1:2 a to zastapila 1:4 bo jak klucz sie nie zmienail to slownik nadpisuje wartosc klucza

# generator to obiekt dlatego zapisujemy go w zmiennej

gen = ((a,b) for a in listA for b in listB if a % 2 ==1 and b % 2 == 0) # aby zrobic generator zamieniamy nawiast kwadratowy od listy na nawias okrągł
print(gen) # gen jest typu generator jest to obiekt programistyczny wykorzysytwany tam gdzie trzeba masakryznie duzo oblcizen zrobic  lista zajmuje miejsce w pamieci a gen nie bo gen to tylko instrukcja jak co ma robic
# aby wyswietlic to co jest opisane w generatorze uzywamy funcki next
print(next(gen)) # zwroci nam pierwsza wartosc aby druga wyswietlic trzeba powielic next
print(next(gen))
# aby nie psiac za kazdym razem next next mozna to zalatwic pętlą for
print('-'*30)
for x in gen:
    print(x) # wyprintuje cala zawartosc gen ale bez peirwszych dwoch bo pierwsze dwi ejuz wczesniej wybralismy poleceniem next(gen)
print('-'*30)
for x in gen:
    print(x) # poraz drugi juz for nic nie wyswietli bo generato sie wyczerpal. generator si ewyczerpuje i juz sie nie odnawia
# trzeba na nowo generator wygenerowac aby znow z niego korzystac
gen = ((a,b) for a in listA for b in listB if a % 2 ==1 and b % 2 == 0)
# inny sposob na wyswietlanie generatora
# tworzymy petle wykounjaca sie w nieskonczonosc
while True:
    try: # musimy to zapakwoac do bloku try bo while w momencie gdy wykorzysta generator a bedzie dalej chcialo dzialac w nieskonczonosc to wywali blad bo generator si eksonczy a to bedzie chcialo dalej dzialac
        print(next(gen))
    except StopIteration: # dla bledu jaki bedzie mowimy ze generator juz pokazal wszystko i przerywamy petle przechwytujemy ten blad i zamist bledu wyswietlamy to co chcemy
        print('All values have been generated')
        break
