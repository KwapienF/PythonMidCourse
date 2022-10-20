class BITException(Exception):  # klasa wyjatków bedow
    #pass # pass czyli pusta intrukcja
    def __init__(self,text,area): # text opis bledu, area miejsce gdzie blad wystapil
        super().__init__(text)
        self.area = area

    def __str__(self):
        return f'{super().__str__()}, area {self.area}'

# sprawdzanie uprawnien
class BitsecurityException(BITException):
    pass

try:
    # do smoething
    raise BITException('File format is incorrect','Financialdata data')
except BITException as e:
    print('Error',e,e.area)
except BitsecurityException as e:
    print('Security Error',e,e.area)


# try:
#     # do smoething
#     raise BITException('File format is incorrect','Personal information')
# except BITException as e:
#     print('Error',e,e.area)
# teraz nie musimy drukwoac e.area bo area zostala zdefiniowana w klasie
try:
    raise BITException('File format is incorrect','Personal information')
except BITException as e:
    print('Aplication Error',e)