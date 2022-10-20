def main():
    with open("/Users/filipkwapien/Desktop/raport.csv") as csv_raport:
        for line in csv_raport:
            print(line)

def main1():
    file = open("/Users/filipkwapien/Desktop/raport.csv", "r")
    text = file.read()
    print(text)

def main2():
    file = open("/Users/filipkwapien/Desktop/raport.csv", "r")
    dane = file.readline()
    while dane != "":
        print(dane)

main2()