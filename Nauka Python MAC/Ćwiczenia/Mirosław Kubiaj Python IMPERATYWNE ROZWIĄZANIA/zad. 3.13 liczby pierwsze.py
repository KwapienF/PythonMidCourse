import math
for i in range(2,150):
     if all(i % a != 0 for a in range(2, int(math.sqrt(i)) +1)):
         print(i)


