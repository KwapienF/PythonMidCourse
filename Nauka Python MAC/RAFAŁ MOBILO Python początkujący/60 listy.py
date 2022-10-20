countries = ['FR', "US", 'DE', 'RU']
print(countries)
print(countries[2]) # tu drukuje nam drugi element listy czyli 3 bo od 0
# APPEND dodanie elementy na koniec do listy APPEND
countries.append('PL')
print(countries)
# INSERT dodanie elementy w dowolne miejsce listy INSERT
countries.insert(2,"ES") # dodan na 3 pozycje bo do 0 liczy
print(countries)
# SORT I REVERSEmozna sortowac elementy listy
countries.sort() # domysleni posortuje od a do z  jak da sie reverse zamiast sort to od z do a
print(countries)
print(countries.reverse)
# POP usuniecie elementow z listy
countries.pop(2)
print(countries)
# REMOVE  pozowli na usniecie elementu z listy ktory sie wskaze samemu POP tylko usuwa element listy znajdujacy sie na konkretnym miejscu
# INDEX sprawdza czy jakis elementy wystepuje i jesli tak to na jakiej pozycji
print('-----------------')
print(countries.index('qq'))
# COUNT policzy ile jest danego elementu w liscie
print(countries.count('PL'))
# LISTA + LISTA stworyz polaczone listy ale niezmieni zadenj z nich
list2 = ['Szwecja', 'Austria']
print(countries + list2)
print(countries)
# LUB EXTEND czyli rozszerzy liste o nową liste i wtedy ta lista juz bedzie zawierala dwie
countries.extend((list2))
print(countries)
# CLEAR czysci liste
list2.clear()
print(list2)
print(countries)
# COPY skopiowanie listy i tworzenie i tworzenie nowej
countires2 = countries.copy()
print(countries)
print(countires2)
countires2.sort()
print(countires2)
countires2.reverse()
print(countires2)

marketing=['loyality program','client promotion','market research']
print(marketing)
marketing.append('public relations')
print(marketing)
print(marketing[3])
marketing.insert(2,'investor relations')
print(marketing)
emailMarketing = marketing.copy()
print(emailMarketing)
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal comunication']
emailMarketing.extend(internalEmails)
print(emailMarketing)
emailTuple = tuple(emailMarketing)
print(emailTuple)
