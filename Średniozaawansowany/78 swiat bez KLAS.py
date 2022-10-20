carBrand = "Seat"
carModel = "Ibiza"
carisAirBagOK = True
carisPaintingOK = True
carisMechanicOK = True

def isCarDamaged(carisAirBagOK,carisPaintingOK,carisMechanicOK):
    return not (carisAirBagOK and carisPaintingOK and carisMechanicOK)

print(isCarDamaged(carisAirBagOK,carisPaintingOK,carisMechanicOK))

# zeby skrocic to co wyzej do jednej zmiennej robimy slownik


car1 = {
carBrand : "Seat",
carModel : "Ibiza",
carisAirBagOK : True,
carisPaintingOK : True,
carisMechanicOK : True
}

car2 = {
carBrand : "KIA",
carModel : "badziew",
carisAirBagOK : True,
carisPaintingOK : True,
carisMechanicOK : False
}

def isCarDamaged(acar):
    return not (acar[carisAirBagOK] and acar[carisPaintingOK] and acar[carisMechanicOK])

print(isCarDamaged(car1)) # przekazuejmy tylko slwonik z informacjami o samochodzie
print(isCarDamaged(car2))
print('-'*50)
# sprawdzenie wszystkich samochodow:
cars = [car1,car2]
for c in cars:
    print(isCarDamaged(c))

# LAB
print('LAB'*40)

cake1 = {
'taste' : 'vanilia',
'glaze' : 'chocolade',
'text' : 'Happy Brithday',
'weight' : 0.7
}

cake2 = {
'taste' : 'tee',
'glaze' : 'lemon',
'text' : 'Happy Python Coding',
'weight' : 1.3
}



def show_cake_info(cakes):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cakes['taste'], cakes['glaze'], cakes['text'], cakes['weight']))


show_cake_info(cake1)
show_cake_info(cake2)



