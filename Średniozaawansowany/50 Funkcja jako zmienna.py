def BuyMe(what):
    print('Give me ',what)
BuyMe('a new car')
StealForMe = BuyMe # bez nawaisow podstawiamy za zmienną
print(type(StealForMe))
StealForMe('a new car')

# robot kelner :
def start(*args):
    print('starting with',*args)

def forward(*args):
    print('going forward with',*args)
def stop(*args):
    print('stop with',*args)

instructions = [start,forward,forward,stop] # lista funckja

for instr in instructions: # instrukcja dla robota z pizza gdzie ma ja zaniesc
    instr('pizza')

# LAB
def double(x):
    return 2 * x
def square(x):
    return x ** 2
def negative(x):
    return -x
def div2(x):
    return x / 2
number = 8
transformations = [double, square, div2, negative]
tmp_return_value = number # tymczasowa zmienna

for trans in transformations:
    tmp_return_value = trans(tmp_return_value)
    print(tmp_return_value)





