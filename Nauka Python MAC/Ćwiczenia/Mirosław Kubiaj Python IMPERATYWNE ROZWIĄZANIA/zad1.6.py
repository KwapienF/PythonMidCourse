import random
from random import randint as losowe
print("Program generuje 5 liczb pseudolosowych z przedziału 1 do 100")
print(losowe(1,100), losowe(1,100), losowe(1,100), losowe(1,100), losowe(1,100))


#inne rozwiazne z pętlą for i funkcją range mówiącą ile pętli ma zrobic

for i in range (5):
    print(random.randint(1,100))
