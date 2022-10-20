import re
if re.match("^[A-Z][a-z]*$", "Ala"):# program ktory dopuszcza pierwsza duza iloscia a potem ile sie chce malych liter
    # gwiazdka * dopuszcza  dany symbol aby pojawil sie wiele raz lub ani razu
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]+$", "Ala"): # symbol plus + pozwala wystapienie danego znaku niskonczona ilosc razy ale ten symbol musi wystapic conajmniej raz a nie jak w gwiazdce ani razu
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]?[A-Z]$", "AllA"): # znak zapytania mowi ze dany symbol  moze wystapic tylko jeden raz lub ani razu
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]{2,5}$", "Ala"): # {2,5} znak moze wystpaic minimum 2 razy ale nie wiecej niz 5 {,5) nie ma minimalnej liczby
    print("Dopasowano")
else:
    print("Nie dopasowano")