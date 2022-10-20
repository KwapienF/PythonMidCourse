def signum():
    x = float(input("Podaj x: "))
    if x < 0:
        sig = -1
    elif x == 0:
        sig = 0
    else:
        sig = 1
    print("signum wynosi", sig)
signum()
