CountryLeaders = {'PL':'DUDA','US':'Trump'} # slwonik  sklada sie z dwoch czesci oddzielonych przecinkiem
# PL jest kluczem a to co po : dwkukropku to wartosc przypisana kluczowi ktora sie wyswietli po jego wskaznaniu
print(CountryLeaders['US']) # do klucza odwolujemy si e w nawiasach []
# można też powiekszyc slownik
CountryLeaders['DE'] = 'Merkel' # doda 3 czesc slownika o kluczu DE i wartosci Merkel
print(CountryLeaders)
print(CountryLeaders.keys()) # wyswietli klucze
print(CountryLeaders.values()) # wyswietli wartosci
print(CountryLeaders.items()) # wyswietli elemetny skaldajace sie  zkluczy i values
# POPITEM  wybierze jeden elementy ze slwonika zwroci go i USUNIE
# SETDEFAULT doda do listy element i wyswietli d aniego wartosc default
print(CountryLeaders.setdefault('FR','Macron'))
print(CountryLeaders)
# GET pokaze values dla wybranego klucza jak go nie ma to tymczasowo pokaze wskazana wartosc
print(CountryLeaders.get('RU')) # none bo nie ma w slowniku tego opisanego setdefault jak nie ma to wyswietli wartosc ale tez doda do slwonika ten element
print(CountryLeaders.get(3, "Tymczasowa dana"))
# UPDATE doda do danej listy nowa zaktualizuje ja o nowe dane a przy powtarzaajcych sie kluczach podmienie values
NewLeadres = {'RU':'Putin', "DE":'Schulz'}
CountryLeaders.update(NewLeadres)
print(CountryLeaders)

