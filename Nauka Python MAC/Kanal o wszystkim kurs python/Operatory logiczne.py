wiek = int(input("Proszę podać wiek: "))
kasa = int(input("Jaką kwotą chce Pan/Pani zapłacić? "))
if wiek >= 18 and kasa >=28:
    print("bilet sprzedano")
elif wiek < 18:
    print(f"Wstęp tylko osobom pełnoletnim, masz o {18 - wiek} lat za mało")
if kasa < 28:
    print(f"Nie można zakupić biletu, brakuje {28 - kasa} zł")
if wiek <18 or kasa < 28:
    print("biletu niesprzedano")


  #  Odwrócenie logiki if not

if True or False and False:
    print("prawda")
else:
    print("fałsz")


