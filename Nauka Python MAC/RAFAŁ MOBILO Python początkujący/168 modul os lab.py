import os
import time
# sciezka pliku /Users/filipkwapien/PycharmProjects/pythonProject2/venv/Nauka Python/RAFAŁ MOBILO Python początkujący/134 LOTTO.py
dir = input('Wprowadz sciezke dostepu do katalogu: ')
print(dir)
if os.path.isdir(dir) is not True:
    print('To nie ścieżka katalogu')
else:
    print("zapisano ścieżkę")
    file = input('Podaj nazwe pliku: ')
    path = os.path.join(dir,file)
    print('Utworzono ścieżkę pliku: ','\n',path)

if os.path.exists(path):
    print('plik istnieje')
    print('Informacje o pliku: ')
    print(time.localtime(os.path.getmtime(path)))
    print(f'rozmiar: {round((os.path.getsize(path)/1024),2)} (MB)')
else:
    print('plik nie istnieje')
