# context manager to cos co pracuajc na czym co zostanie otwarce zawsze to pozniej zamknie i ty nie musisz o tym pameitac np wuth open file. jak sam otworzysz plik to musisz go zamkanc a with samo tego pilne with open file to wlasne context manager

with open(r'C:\temp\view.txt', 'w+') as file:
    file.writelines('SUCCES')
#nie trzeba close bo sie zamknelo samo

# prba zbudowania wlasnego contet managera
import time
class time_measurre:
    def __init__(self):
        pass
    def __enter__(self): # metoda enter to ta ktora wywoluje sie w momencie keidy obiekt jest tworzony
        print('entering...')
        self.__start = time.time() # ukryta mzmienna instancji
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting...')
        self.__stop = time.time()
        self.__difference = self.__stop - self.__start
        print(f'Execution time {self.__difference}')

with time_measurre() as my_timer:
    time.sleep(3)
