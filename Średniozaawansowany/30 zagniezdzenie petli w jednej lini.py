listA = list(range(0,10))
listB = list(range(1,10))
print(listA,listB)

product = []
for a in listA:
    for b in listB:
        product.append((a,b))
print(product)
# to samo w jednej lini
product = [(a,b)for a in listA for b in listB]
print(product)
# aby wyswietlic nieparzyste w a i parzyste w listb
product = [(a,b)for a in listA for b in listB if a % 2 ==1 and b % 2 == 0]
print(product)
# slownik
product = {a:b for a in listA for b in listB if a % 2 ==1 and b % 2 == 0}
print(product) # w slowniku nadpisuja sie wartosci dla klucza dlatego mamy 1:4 w wyniu bo 1:0 zastapilo 1:2 a to zastapila 1:4 bo jak klucz sie nie zmienail to slownik nadpisuje wartosc klucza
