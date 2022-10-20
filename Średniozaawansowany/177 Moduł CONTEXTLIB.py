import contextlib
# jak zbudowac context managera ktory nie bedzie korzystal z metody enter

class Door:
    def __init__(self,where):
        self.where = where

    def open(self):
        print('Opening door to the {}'.format(self.where))
    def close(self):
        print('Closing door to the {}'.format(self.where))

door1 = Door('hell')
door2 = Door('future')

door1.open()
door1.close()
door2.open()
door2.close()
from contextlib import contextmanager # dzieki dekoratorowi kazda funckja bedzie context managerem i nie bedie bledu o tym ze nie ma funcki enter lub exit
@contextmanager
def OpenAndClose(obj):
    obj.open()
    yield obj # zwracamy ten obiekt yield aby funckaj sie w tym momecnie zamrozila i poczekala az co s z tym zwroconym obiektme zrobimy np funkcją with jak ponizej a jak to zakonczymy to pojdzie dalej
    obj.close()

with OpenAndClose(Door('next room')) as door:
    print('The door is to the {}'.format(door.where))
print('-'*100)
from urllib.request import urlopen
from contextlib import closing

with closing(urlopen('http://www.kursyonline24.eu')) as page:
    for line in page:
        print((line))

import os
# os.remove(r'c:\temp\not_used_file.txt') # funkcja zwroci blad jezeli nie ma pliku ktorego trzeba usuanc mozna try exept ale mozna inacz:
from contextlib import suppress # suppres to funkcja ukrywająca błędy
with suppress(FileNotFoundError): # jezeli ne ima pliku to nie pokaze bledu program
    os.remove(r'c:\temp\not_used_file.txt')

from contextlib import redirect_stdout # jezeli co stworzy dodatkowy output  wyswietlaja cos na ekranie to mozemy ten dodatkowy komunikat umiescic w pliku zamiast go wyswietlac w programie
f = open(r'c:\temp\log.txt','w')
with redirect_stdout(f):
    print('Hello') # zamiast wyprintowac hello w programie to zapsize ten komunikat w pliku txt 
