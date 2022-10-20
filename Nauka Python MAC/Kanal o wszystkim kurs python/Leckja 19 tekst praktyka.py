file = open("/Users/filipkwapien/Desktop/covid.txt", "r")
text = file.read()
file.close()

def policz_litery(txt, znak):
    licznik = 0
    for z in txt:
        if z == znak:
            licznik +=1
    return licznik

print(policz_litery(text,"a"))
print(policz_litery(text.lower(),"a")) # zmieniamy wszystkie litery na a aby policzyc duze A i male a razem


for znak in "abcdefghijklmnopersuwxyzq., ":
    procent = 100 * policz_litery(text.lower(), znak) / len(text)
    #print("procent = %5.2f"% procent,"%")
    print("{0} - {1} - {2}".format(znak.upper(),policz_litery(text.lower(), znak),"%5.2f"% procent + "%" ))

print("procent ", round((policz_litery(text.lower(), "a") / len(text) * 100), 2), "%") # round(co?, 2) zaokrągla do miejsc po przecinku


