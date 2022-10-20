import os

class ini_file:
    def __init__(self,path):
        self.path = path
        self.parameters = {} # słownik w ktorym bedzemy przechowwyac raz odczytane dane znajdujace sie w pamieci pliku
        self.read_fromdisk() # metoda odpowiedzialna za odczyt danych z pliku
    def read_fromdisk(self):
        if os.path.isfile(self.path):
            with open(self.path) as file:
                for line in file:
                    parts = line.replace("\n",'').split('=')
                    self.parameters[parts[0]] = parts[1] # instrukcja aktualizująca słownik
    def read_parameter(self,key): # pobieranie parametrow
        if key in self.parameters.keys(): # sprawdzamy czy dany kluc zjest na liscie klcuzy w anszym slwoniku
            return self.parameters[key]
        else:
            return None

    def write_parametr(self,key,value):
        self.parameters[key] = value
    def save_on_disk(self): # aktualziauje plik i zapisuje na dysku
        with open(self.path,'w') as file:
            for key, value in self.parameters.items():
                line = "{}={}\n".format(key,value)
                file.writelines(line)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb): # exp type typ bledu, exp value  wartos bledu np invalida rgument, exepctio traceback powiazanie bledu z byc moze wczesniejszymi bledami
        print('exit')
        print('exc_type = {}'.format(exc_type))
        print('exc_value = {}'.format(exc_val))
        print('exc_traceback = {}'.format(exc_tb))
        if exc_type == OSError: # jezeli exit w typ bledu zwraca true to blad jest ukryty jeeli nadamy  jakiemus bledowi Fasle to zozstanie on pokaany nam "na zewnatrz"
            return False
        else:
            return True # true mowi podajmy ze nic zlego sie nie stalo ukryjmy blad


with ini_file(r'c:\temp\my.ini') as myini:
    myini.write_parametr('mode','strict')
    myini.write_parametr('loglevel', 'light')
    myini.save_on_disk()
    print(10/0) # dojdzie do bledu ale nie pokaze bledu tylko wyprintuje nam to co chcielismy w funkcji exit

