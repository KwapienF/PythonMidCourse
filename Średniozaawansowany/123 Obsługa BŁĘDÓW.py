clients = {
    "INFO": 0.5,
    "DATA": 0.2
}

myClient = input('Clients NAME: ')
totalCost = 7200

# obsluga bledy na wyapdek gdy wprowadzimy nazwe ktorej nie ma w slowniku
try:
    print("The % ratio for {} is {}".format(myClient,clients[myClient]))
except Exception as e: # dostane do dyspozycji zmienną e ktora bedzie instancja klasy Exception i wtedy bedziemy mogli wyswietlic to co jest w tej klasie
    print('Client NOT FOUND','\n',e)
else: # else przy TRY wykona sie wtedy kiedy w try nie wystapil blad
    print("The cost for {} is {}".format(myClient,clients[myClient] * totalCost))
finally: # finally wykona sie zawsze
    print('THE END')