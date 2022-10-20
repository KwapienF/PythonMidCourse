def trojka_pitagorejska(a,b,c,):
    if a * a + b * b == c * c:
        print("ok")
    else:
        print("nie ok")

def main():
    a = int(input("podaj a: "))
    b = int(input("podaj b: "))
    c = int(input("podaj c: "))
    trojka_pitagorejska(a,b,c)
main()
