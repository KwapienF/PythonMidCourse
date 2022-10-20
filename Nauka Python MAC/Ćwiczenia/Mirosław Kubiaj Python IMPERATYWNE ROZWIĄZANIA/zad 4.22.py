def dodaj_do(x):
    def dodaj(y):
        return x + y
    return dodaj

def main():
    dodaj_do_15 = dodaj_do(15)
    print(dodaj_do_15(20))
    print(dodaj_do(15)(20))
main()


def program1(x):
    def program2(y,z):
        return x + y - z
    return program2

def main2():
    print(program1(1)(2,3) * 2)
main2()