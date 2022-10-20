class Sortowanie:
    def __init__(self,lista):
        self.lista = lista
        print("Sortowanie bąbelkowe poniższej listy:")
        print(lista)
    def __del__(self):
        print("Zakończenie programu i zwolnienie pamięci")
    def sort_data(self, lista):
        self.lista = lista
        print("Posortowana lista poniżej: ")
        j = 0
        while j < len(lista)-1:
            i = 0
            while i < len(lista)-1:
                if lista[i] > lista[i+1]:
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                i += 1
            j += 1
        print(lista)
def main():
    lista = [547, 303, -134, 125, 80, 236]
    program = Sortowanie(lista)
    program.sort_data(lista)
main()
