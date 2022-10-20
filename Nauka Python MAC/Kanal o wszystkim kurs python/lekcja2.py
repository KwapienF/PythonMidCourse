import math #importujemy moduł math aby wykonywac np. pierwiastkowanie
# num1 = 5
# num2 = 31
# suma = num1 + num2
# różnica = num1 - num2
# iloraz = num1 / num2
# iloczyn = num1 * num2
# potęgowanie = num1 ** num2
# print(suma)
# print(różnica)
# print(iloraz)
# print(iloczyn)
# print(potęgowanie)
# # int #liczby całkowite 2,4,-2, itd
# # float #liczby zmiennoprzecinkowe
# ilorazcalkowity = num2 // num1 # 2 znaki dzielenia pokazuje ile razy zmiesci sie liczb calkowitych bez reszty w wyniku
# print(ilorazcalkowity)
# dzielenieModulo = num2 % num1 # pokauzje reszte ile zostało z dzielenia jak 31/5 to 1 bo 31-6*5 można to wykorzystac do sprawdzenia czy liczba jest parzysta czy nie
# print(dzielenieModulo)
# print(f"Wynik dzielenia {num2} przez {num1} to {ilorazcalkowity} całych oraz {dzielenieModulo} reszty")
# num3 = 36
# #pierwiastkowanie na 2 sposoby
# pierwiastek = num3 ** 0.5 # pierwiastek 2 stopnia
# print(type(pierwiastek)) # pokazuje typ liczby wyniku
# print(pierwiastek)
# #we float są miejsca po przecinku można rzucić w int i będą liczby całkowite:
# print(int(pierwiastek))
# #2 sposób peirwiastkowania - zaimportowanie modułu na początku kodu:
#
# pierwiastekMath = math.floor(math.sqrt(num3)) # funkcaj floor w module math zaokragla w dol liczbe, ucina to co po przecinku
# print(pierwiastekMath)
# pierwiastekRound = round(math.sqrt(num3)) # round zaokrągla
# print(pierwiastekRound)
# num4 = 49
# num4 += 4  # skrótowy zapis działania num4 = num4 + 4  += -+ /= itd **=
# print(num4)
# # interakcja z użytkownikiem funcka input(zawsze wywali stringa)

print("Witaj, wpisz liczbę, a ja powiem Ci ile jej całości mieści się w liczbie, którą wybierzesz i ile reszty zostanie")
digit= float(input()) # uzwyamy float bo przy int wywali błąd jakktos wpisze liczbe po przecinku
print("Dziękuję",f"Wpisałeś liczbę:{digit}", sep="\n")
a = 999 // digit
b = 999 % digit
print(f"Wynik dzielenia liczby 999 przez Twoją liczbę {digit} daje nam {int(a)} liczby całkowitej oraz resztę {b}")



