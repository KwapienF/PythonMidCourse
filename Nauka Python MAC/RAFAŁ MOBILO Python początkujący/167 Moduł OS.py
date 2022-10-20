import os # wykonuje czynnosci zwizne ze sciezkami dostepu do plikow
import time
#GETCWD pokazuej info o biezacym katalogu w ktroym jest zapisany program
print("current directory is",os.getcwd())
#tworzenei nazwy sciezki pliku OS.PATH.JOIN
currentdir = os.getcwd()
filnename = 'results'
fullpath = os.path.join(currentdir, filnename)
print(fullpath)
# OS.PATH.ABSPATH pokaze bezwgledna sciezke pliku czyli od katalogu np C
print(os.path.abspath('ra woj'))
# BASENAME wyswieyi nazwe pliku a DIRNAME nazwe katalogu w ktorym jest plik to wszystko ze sciezki pliku
print(os.path.basename(fullpath))
print(os.path.dirname(fullpath))
#OS.PATH.EXISTS zy plik w orkeslonej scieze istnieje czy nie
print(os.path.exists(fullpath)) # false bo nie ma takiego pliku
print(os.path.exists(r'/Users/filipkwapien/PycharmProjects/pythonProject2/venv/Nauka Python/RAFAŁ MOBILO Python początkujący/134 LOTTO.py')) # true bo jest taki
#OS.PATH.GETMTIME data utworzenia modyfikacji lub ostatenigo dostepu do pliku
# time trzeba w pythonie skonwertowac do LOCALTIME bo inaczej pokaze czas od daty unixa a nie normalny
path1 = r'/Users/filipkwapien/PycharmProjects/pythonProject2/venv/Nauka Python/RAFAŁ MOBILO Python początkujący/'
print(time.localtime(os.path.getmtime(path1)))
# GETSIZE  wyswietli w bajtach ilosc
print(os.path.getsize(path1))
# ISDRI czy to jest katalog lub ISFILE czy to jest plik pokaze true lub nie
print(os.path.isdir(path1))
print(os.path.isfile(path1)) # true bo jest to sciezka do pliku a nie sama sciezka
# OS.PATH.SPLIT oderwuje nazwe sciezki od katalogu i utworzy tuple bo w () lista jest w [] ;)
print(os.path.split(path1))
#SPLITDRIVE zwrocu tuple gdzie bedzie nazwa dysku i sicezka dostepu do pliku
print(os.path.splitdrive(path1))
# mozna tez
print('drive is: ',os.path.splitdrive(path1)[0]) # [0] pokaze tylko nazwe dysku bo wyswietli element zerowyz  tuple
