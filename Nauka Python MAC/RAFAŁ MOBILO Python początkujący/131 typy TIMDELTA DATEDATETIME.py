import datetime # potezny module
print(datetime.MINYEAR, datetime.MAXYEAR) # pokazuje jaka jest wtym moduel min i max wartosc dla roku
# TIMEDELTA liczy nam roznice czasu
d1 = datetime.timedelta(days=1,hours=2,minutes=-30) # co to znaczy? ze ktoc cos zrobi za 1 dzien 2 gdzoiny bez 30 minut czyli python poakze nam 1 dzien i godzine trzydzisci
print(d1)
# ktos mowi ze to bylo wczoraj, 2 godziny wczesniej i 3 minuty wczesnie
d2 = datetime.timedelta(days=-1,hours=-2,minutes=-3) # python pokaze to jako -2 dni + 21 gdzoin i plus 57 minut
print(d2)
# datetime to wektor czasu o ktory musimy sie przesuanc do przodu lub do tylu


# DATA = DATE

today = datetime.date.today() # data dzisiejsza
print('today is',today)
# jesli faktura ma byc platna za 7 dni to
pay = datetime.timedelta(days=7)
payday = today + pay
print(payday)

# ile dni zyla babcia?
born = datetime.date(1935,5,20)
days = today - born
print(days)
born2 = datetime.date(1989,5,31)
days2 = today - born2
print(days2)
# wyswietlanie daty i godziny jednoczesnie:
print(datetime.datetime.now()) # daje date i godzine now i today daje rozny czas w zaleznosci od strefy czasowej
print(datetime.datetime.today())
print(datetime.datetime.utcnow()) # czas ogolny  na ktory nie ma wpywu strefa czasowa
print(datetime.datetime.today().weekday())
# STRFTIME  konwertuje liczbe modulow dat do napisow np aby dni tygodnia wyswietlalo nazwami  a nie liczbami
print(datetime.datetime.now().strftime('%a'))# %a oznacza ze pokaze skrocona nazwe tygodnia a nie pełną %A da pelna nazwe
print(datetime.datetime.now().strftime('%A'))
print(datetime.datetime.now().strftime('%w')) # numer dnia tygodnia i tutaj liczymy niedziele jako dzien zerowy!!!!!!

# WAZNE:
print(datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f'))
# %Y rok przy uzyciu 4 cyfr
# %m miesiac przy uzyciu 2
# %d  dzien przy uzyciu 2
# %H godzina przy uzyciu 2 cyfr w formacie od 0 do 23
# %M minuty przy uzyciu 2 cyfr
# %S sekundy przy uzyciu 2 cyfr
# %f milisekundy pokaze