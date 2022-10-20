clients = {
    "INFO": 0.5,
    "DATA": 0.2
}

myClient = input('Clients NAME: ')
totalCost = 7200

# obsluga bledy na wyapdek gdy wprowadzimy nazwe ktorej nie ma w slowniku
try:
    ratio=float(input("Enter new ratio: "))
    print("The % ratio for {} is {}, a new one is {}".format(myClient,clients[myClient],ratio))
    print("The cost for {} is {}".format(myClient,ratio * totalCost))
    print('New ratio compare to old one: {}'.format(clients[myClient]/ratio))
except KeyError as e: # jak wprowadzimy zlego klienta
    print(f'Wrong Client, client is not for a list {[c for c in clients.keys()]}',e)
# except ValueError as e:
#     print('it must be a NUMBER',e)
except (ZeroDivisionError, ValueError) as e: # można łączyć błędY!
    print('Cant div by 0!',e)
except Exception as e: # dostane do dyspozycji zmienną e ktora bedzie instancja klasy Exception i wtedy bedziemy mogli wyswietlic to co jest w tej klasie
    print('Client NOT FOUND','\n',e)