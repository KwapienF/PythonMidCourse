x = 12
y = 2
try: # oznacza spróbuj wykoanc te operacje ale nie muszą one sie udac
    lista = [4,5]
    print(lista[0])
    print(x + 4)
    print(x / y)
    print("linijka po")
except ZeroDivisionError: # mozna w nawiasie zaznacyz wiecej wyjatkow (zerdiv, typerror):
    print("nie dziel przez 0")
except TypeError:
    print("błąd typu danych, są niezgodne")
except: # bez zdefiniowania wyjatkow  tutaj wrzuca wszystkie inne wyjatki
    print("inne jakies wyjatki")
finally: #nieobowiazkowy ale daje sie go dla lepszej czytelnosci kodu i sluzy do zakonczenia zadania bloku try jak jakis wyjatek bedzie to finally sie wykona zawsze
    print("koniec")
print("dalsze instrukcje:")
