import math
import random
import datetime
from turtle import * # * oznacza ze improtuje wszystkie funckje z turtle
def main(): # definiuje funkcje o nawie main
    start = datetime.datetime.now() # odczytuje czas z systemu operacyjnego
    print("Aktualna data i czas z SO: ", end = "" )
    print(start)

    # wykres graficzny obliczeń
    title("Pi  Monte Carlo")
    setup(width=640, height=470)
    bgcolor("black")
    penup()
    hideturtle()
    speed(0) # maksymalna szybkosc rysowania
    def makedot(dotcolor):
        goto(round(x*100 - 100), round(y*100 - 100)) # zaokraglamy liczby bo piksele ni ema ja miejc po przecinku i skalumey bo round od 0-2 da malo wynikow
        dot(3, dotcolor) # -100 wyzej bo przesuwamy o 100 pikseli aby rysowalo nam na srodku okna a nie w cwiartce
    punkty = 100
    licznik = 0
    print("Trwają obliczenia")
    print()
    for i in range(1, punkty,1):
        x = random.uniform(0,2)
        y = random.uniform(0,2)
        if math.sqrt((x -1)**2 + (y -1)**2) <=1:
            licznik = licznik +1 # sprawdza czy punkty znajdują się w kole o promieniu <=1
            makedot('red')
        else:
            makedot('white')
    pi = 4.0 * licznik/punkty # oblciza pi
    print("stała pi = ", math.pi)
    print(f"Obliczona wartość pi =  {pi:.8f}")
    print("Różnica = ", math.pi - pi)
    print()
    stop = datetime.datetime.now()
    print("Czas obliczeń: ", stop - start)
    print("KONIEC")
    done()
main()



