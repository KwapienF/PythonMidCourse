lista = [1,2,3,4,5,6,7,8,9,10,11]  # suma od 3 do 10 rekurencją
def sum(lista,p,k):
    if p > k:
        return 0
    else:
        return lista[p] + sum(lista,p +1,k)

def main():
    p = 3
    k = 10
    print(sum(lista,p,k))
main()


