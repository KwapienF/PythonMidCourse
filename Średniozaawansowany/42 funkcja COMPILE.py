#eval i excec bierze tekst i przerabia na czesc programu
# compile
import time

source = "reportLine += 1"
reportLine = 0
start = time.time()
for i in range(100000):
    exec(source)
stop = time.time()
time_not_compiled = stop - start


# kompilujemy aby np przy raporcie ktory ma 1000 linijek  excec nie wykonywal progrmay 1000 razy
# rekompilujemy fragment tekstu
start2 = time.time()
sourceCompile = compile(source, 'internal variable source', 'exec' ) #1 parametr to co chcemy skomilowac drug parametr to plik lub danan z programu 3 parametr to tryb mode  excec lub eval
# wpisalismy interna var source bo liku nie posiadamy wiec info ze z wewnetrznego zrodla pobieramy dane
for i in range(100000):
    exec(sourceCompile)
stop2 = time.time()
time_compiled = stop2 - start2
print(time_not_compiled)
print(time_compiled)
print(time_not_compiled/time_compiled)