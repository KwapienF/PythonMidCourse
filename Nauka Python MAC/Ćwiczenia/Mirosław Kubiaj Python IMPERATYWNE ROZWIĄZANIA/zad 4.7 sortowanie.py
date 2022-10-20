from random import randint
def sortowanie(n):
    lista = []
    for x in range(n):
        x = randint(-1000,1000)
        lista = lista + [x]
    print(lista)
    print("Lista posortowana od min do max:")
    lista.sort()
    print(lista)
    print("Lista posortowana od max do min:")
    lista.reverse()
    print(lista)
def main():
    n = int(input("Podaj ilość liczb: "))
    sortowanie(n)
main()
