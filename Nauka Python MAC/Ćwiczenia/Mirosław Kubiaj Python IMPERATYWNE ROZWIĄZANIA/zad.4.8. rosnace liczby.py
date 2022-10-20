
x = 0
while x <= 5:
    y = x + 1
    print("dla x =", x, " y =", y, sep = "\t")
    x += 0.5

# to samo z wykorzystaniem lambda
def main():
    oblicz = lambda x : x * x +1
    krok = 0.5
    x = 0
    print()
    while x <= 5:
        y= oblicz(x)
        print(f'x = {x:.2f},', '\t', f'y = {y:.2f}.')
        x+= krok
main()
