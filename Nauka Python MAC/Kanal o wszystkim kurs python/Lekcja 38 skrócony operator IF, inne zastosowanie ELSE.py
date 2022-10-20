print("prawda") if 5 < 2 else print("Fałsz")
a = "Parzysta" if 10 % 2 == 0 else "Nieparzysta" # nie trzeba uzywac print mozna wyprintowac zmienna zapytania
print(a)


# inne wykorzystnie słówka else

for i in range(10):
    if i > 5:
        continue  # zamiast break dajemy contiune aby petla szla dalej po spelnieniu warunkow
else: # to else tyczy sie petli FOR
    print("Koniec1")
try:
    a = 5/0
except ZeroDivisionError:
    print("Błąd")
else:
    print("Koniec2") # else zadziala jak try sie wykona a tu sie nie wykonalo
finally: # finally zawsze sie wykona na koniec niezaleznie czy cos zostnaie spelnione czy nie
    print("Zawsze")