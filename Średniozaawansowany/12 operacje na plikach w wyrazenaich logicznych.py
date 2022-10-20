import os

path = r'c:\temp\mydata.txt'
#os.remove(path)
'''
if os.path.isfile(path):
    print('File %s exists' % path)
else:
    print('Creating a file %s' % path)
    open(path,'x').close() # x oznacza, ze w przypadku gdyby taki plik juz istnial to ma byc zgloszony blad. Po otwarciu jest cloe bo zalezalo nam tylko aby go utworzyc ten plik dlatego zaraz po otwarciu go sie utworzyl wiec od razu go zamykamy
    print('File %s created' % path)'''
# inny sposób
result = os.path.isfile(path) or open(path,'x').close() # zwroci none bo python sprawdza wszystko dla result pierw jest falsz bo nei istnieje plik pozniej aby sprawdzic drugi warunek musi go wykoanc wiec tworzy plik i zaraz go zamyka wyswieti NONE bo close zwraca bool none
print(result)
# jak plik istnial to pierwszy czlon python zinterpretowal jako TRUE bo plik istnieje. Drugiego juz nie sprawdzal wiec nie utowrzyl kolejengo tego samego pliku bo
# jest to warunek logiczny alternatywa czyli jak choc jeden jest TRUE warunek to wynik jest TRUE skorow  pierwsyzm czlonie mial juz true to nie sprwadzal juz drugiego bo i tak by bylo true
