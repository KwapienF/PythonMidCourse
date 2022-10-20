# python sie zmienia juz nie dziala clock jak obejsc ten problem? a tak:

import time
# sprawdzenie wersji pythona
import sys
# zamiast
# print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
print(time.perf_counter(), time.localtime(time.perf_counter()))


#LEKCJA

print(sys.version)
print(time.time()) # pokaze nam czas unixowy
print(time.localtime(time.time())) # 0 poniedzialek 1 wtorek 2 sroda 3 czwartek 4 piatek tm_yday mowi ktory to dzien w roku a tm_isdst  czas letni jezeli 1. ta funkcja tworzy tuple
# time for human readable
print(time.asctime(time.localtime(time.time())))
import calendar
print(calendar.month(2022,8,w=5,l=2)) # w=5 na kazdy dzien jest 5 znakow odstepu, l=2 odstepy miedzy dniami to to 2 spacje jezeli nie podasz w i l to wydrukuje minimalne odstepy jak nizej
print(calendar.month(2022,8))
# jaki dzien tygodnia byl okreslonego dnia? funkcja weekday(rok,miesiac, dzien)
print(calendar.weekday(1935,5,20)) #0 wyjdzie czyli monday
#funkcja setfirstweekdday(6) pozwoli nam ustawic aby poniedzialek nie byl pierwsyzm dzneim tygodnia tylko bedzie nim dziele czyli 6
calendar.setfirstweekday(6) # wplywa tylko na to od jakiego dnia narysuje sie kalendarz tutaj od niedzieli = 6 i nie wplywa jak liczone sa dni tygodnia poniedzialek dalej bedzie 0
print(calendar.month(2022,8))
print(calendar.isleap(2020)) # wskaze true or False czy wskazany rok jest przestepny
print(calendar.leapdays(2000,2022)) # wskaze ile bylo dni przestepnych w podanych latach !!!! lepadays liczy od roku 2000 ale drugi podany rok juz nie wlicza czyli do 2022 bez 2022
print(calendar.calendar(2023)) # pokaze kalendarz za caly rok :D




