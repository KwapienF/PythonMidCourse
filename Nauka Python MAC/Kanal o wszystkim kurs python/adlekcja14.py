plik1 = open("/Users/filipkwapien/Desktop/test.txt", "r")
if plik1.readable():
    for l in plik1:
        print(l)