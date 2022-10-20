a = 5
b = 5
operacja = "dodawanie"
if operacja == "dodawanie":
    wynik = a + b
else:
    wynik = a - b
print(wynik)

# to samo za pomocą operatora trójargumentowego:
operacja2 = "dodawanie"
wynik2 = (a + b) if operacja2 == "dodawanie" else (a - b)
print(wynik2)

imie1 = "Filip" # można uzyc " lub ' w stringu
imie2 = 'Lecia'
imiona = "Imiona różnia się" if imie1 != imie2 else "Imiona są takie same"
print(imiona)