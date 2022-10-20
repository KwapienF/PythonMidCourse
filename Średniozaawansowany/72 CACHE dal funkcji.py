import time
import functools
@functools.lru_cache() # dekorator nie bedzie liczyl dwa razytych samych rzeczy w funkcji ktora dekoruje, zapameituje wyniki juz wykonanych obliczen
def Factorial(n):
    time.sleep(0.1) # opoznienei dzialania funckji aby dluzej sie robila
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)

start = time.time()
for i in range(1,11):
    print(i, Factorial(i))
stop = time.time()
print(stop - start)

print(Factorial.cache_info()) # funckja zworcu ile wynikow zostalo skeszowanych i ile razy z tych wynikow skorzystala cache.info() cursize current ile wynikow otrzymalismy maxsize ile wynikow max moze przechwoac casch jego wielksoc mozna w dekoratorze zmienic domyslnie jest 128
# misees ile razy nie udalo sie znalezc wynikow w cacheu
#hits ile razy skorzystalismy z wynikow z cache
# funckja korzystająca z cache musi byc deterministyczna czyli odwolywac sie do tych samych wynikow i zmienncyh nie mzoe byc nap czas ktory bedzie zawsze inny lub zmienne losowe itd



# aby skrocic czas dzialania tej funckji korzystamy z functools.


# lab
print('-'*50)
@functools.lru_cache(100) # max moze zapamietac 100 wynikow
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start = time.time()
for i in range(1,11):
    print(fib(i))
stop = time.time()
print(stop - start)

print(fib.cache_info())