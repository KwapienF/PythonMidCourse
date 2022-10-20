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
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

ini = ini_file(r'c:\temp\my.ini')
ini.write_parametr('version',1)
ini.write_parametr('level','advanced')
ini.save_on_disk()
# jak odczytywac etraz plik?

ini2 = ini_file(r'c:\temp\my.ini')
print(ini2.parameters)
print(ini2.read_parameter('version'))
print(ini2.read_parameter('level'))
# korzystanie z tej klasy jak z context managera:
with ini_file(r'c:\temp\my.ini') as ini3:
    print(ini3.parameters)
    print(ini3.read_parameter('version'))
    print(ini3.read_parameter('level'))

